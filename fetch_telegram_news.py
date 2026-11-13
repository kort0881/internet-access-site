#!/usr/bin/env python3
"""
Забирает последние посты из публичного Telegram-канала @vlesstrojan
и сохраняет их в telegram_news.json для build.py.

Работает без api_id/api_hash и без сессии: используется публичная
веб-версия канала https://t.me/s/<channel>.

Переменные окружения (все необязательные):
  TG_CHANNEL       — имя канала без @ (по умолчанию vlesstrojan)
  TG_POSTS_LIMIT   — сколько постов брать (по умолчанию 10)
  TG_NEWS_FILE     — куда писать JSON (по умолчанию telegram_news.json)
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from html import unescape

import requests

CHANNEL = os.environ.get("TG_CHANNEL", "vlesstrojan").lstrip("@").strip()
POSTS_LIMIT = int(os.environ.get("TG_POSTS_LIMIT", "10") or 10)
NEWS_FILE = os.environ.get("TG_NEWS_FILE", "telegram_news.json")

PREVIEW_URL = f"https://t.me/s/{CHANNEL}"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ru,en;q=0.9",
}

MONTHS_RU = [
    "", "января", "февраля", "марта", "апреля", "мая", "июня",
    "июля", "августа", "сентября", "октября", "ноября", "декабря",
]


def fetch_html(url: str, timeout: int = 20) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def _extract_div(html: str, start: int):
    """Возвращает (внутренний html, индекс после закрывающего </div>).

    start указывает на начало открывающего тега <div.
    Учитывается вложенность div.
    """
    depth = 0
    i = start
    inner_start = None
    tag_re = re.compile(r"<div\b|</div\s*>", re.IGNORECASE)
    for m in tag_re.finditer(html, start):
        if m.group(0).lower().startswith("</"):
            depth -= 1
            if depth == 0:
                return html[inner_start:m.start()], m.end()
        else:
            depth += 1
            if depth == 1:
                # конец открывающего тега
                gt = html.find(">", m.end())
                if gt == -1:
                    return "", len(html)
                inner_start = gt + 1
    return "", len(html)


def strip_html(fragment: str) -> str:
    """Убирает теги, сохраняя переводы строк и раскрывая HTML-сущности."""
    text = re.sub(r"(?i)<br\s*/?>", "\n", fragment)
    text = re.sub(r"(?i)</p\s*>", "\n", text)
    text = re.sub(r"(?i)</div\s*>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = text.replace("\u00a0", " ")
    # нормализуем пустые строки
    lines = [ln.strip() for ln in text.splitlines()]
    text = "\n".join(ln for ln in lines if ln)
    return text.strip()


def format_date(iso_ts: str) -> str:
    """ISO-таймстемп из <time datetime=...> -> '13 ноября 2026'."""
    try:
        dt = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return f"{dt.day} {MONTHS_RU[dt.month]} {dt.year}"
    except Exception:
        return datetime.now().strftime("%d.%m.%Y")


def make_title(text: str, limit: int = 100) -> str:
    first = text.splitlines()[0].strip() if text else ""
    first = re.sub(r"\s+", " ", first)
    if len(first) > limit:
        cut = first[:limit].rsplit(" ", 1)[0]
        first = (cut or first[:limit]).rstrip(" ,.;:—-") + "..."
    return first


def make_summary(text: str, limit: int = 300) -> str:
    flat = re.sub(r"\s+", " ", text.replace("\n", " ")).strip()
    if len(flat) > limit:
        cut = flat[:limit].rsplit(" ", 1)[0]
        flat = (cut or flat[:limit]).rstrip(" ,.;:—-") + "..."
    return flat


def parse_posts(html: str, limit: int):
    """Достаёт посты из HTML веб-превью канала."""
    posts = []
    # каждый пост — обёртка <div class="tgme_widget_message ..." data-post="channel/123"
    wrap_re = re.compile(
        r'<div[^>]*class="[^"]*tgme_widget_message\b[^"]*"[^>]*data-post="([^"/]+)/(\d+)"',
        re.IGNORECASE,
    )
    matches = list(wrap_re.finditer(html))
    for idx, m in enumerate(matches):
        msg_id = int(m.group(2))
        body, _ = _extract_div(html, m.start())

        text = ""
        tm = re.search(r'class="[^"]*tgme_widget_message_text\b', body)
        if tm:
            tag_start = body.rfind("<div", 0, tm.start())
            inner, _end = _extract_div(body, tag_start)
            text = strip_html(inner)

        if not text:
            continue

        time_m = re.search(r'<time[^>]*datetime="([^"]+)"', body)
        date_iso = time_m.group(1) if time_m else ""

        posts.append({
            "id": msg_id,
            "date": format_date(date_iso),
            "date_iso": date_iso,
            "title": make_title(text),
            "summary": make_summary(text),
            "link": f"https://t.me/{CHANNEL}/{msg_id}",
            "source": f"Telegram @{CHANNEL}",
        })

    posts.sort(key=lambda p: p["id"], reverse=True)
    return posts[:limit]


def save(posts) -> None:
    with open(NEWS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    print(f"✅ Сохранено {len(posts)} постов в {NEWS_FILE}")


def main() -> int:
    print(f"📡 Читаю публичную ленту {PREVIEW_URL} (без api_id/api_hash)")
    try:
        html = fetch_html(PREVIEW_URL)
    except Exception as e:
        print(f"⚠️ Не удалось получить ленту Telegram: {e}")
        print("⚠️ Оставляю прежний telegram_news.json (если есть), сборка пойдёт на fallback")
        return 0

    posts = parse_posts(html, POSTS_LIMIT)
    if not posts:
        print("⚠️ Посты не найдены (канал закрыт или разметка изменилась)")
        return 0

    save(posts)
    print(f"✅ Получено {len(posts)} постов из @{CHANNEL}")
    newest = posts[0]
    print(f"   последний: {newest['date']} — {newest['title'][:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
