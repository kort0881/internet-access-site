#!/usr/bin/env python3
"""Static site generator for GitHub Pages deployment."""

import os
import shutil
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from services import get_vpn_configs, get_last_update_time
import feedparser

# Конфигурация
DIST_DIR = Path('dist')
TEMPLATES_DIR = Path('templates')
STATIC_DIR = Path('static')

# SEO (RU)
META_TITLE = "Доступ к интернету - Свободный доступ в сеть"
META_DESCRIPTION = (
    "Автоматические конфигурации для V2Ray, VLESS, Hysteria, Trojan, VMess, Reality и Shadowsocks. "
    "Регулярное обновление, удобные ссылки, стабильное соединение."
)
META_KEYWORDS = "доступ к интернету, свободный доступ в сеть, vless, v2ray, shadowsocks, hysteria, trojan, vmess, reality, конфигурации"

# SEO (EN)
META_TITLE_EN = "Internet Access - Free Internet Access"
META_DESCRIPTION_EN = (
    "Automatic configurations for V2Ray, VLESS, Hysteria, Trojan, VMess, Reality and Shadowsocks. "
    "Updated regularly, easy subscription links, stable connection."
)
META_KEYWORDS_EN = "internet access, free internet access, vless, v2ray, shadowsocks, hysteria, trojan, vmess, reality, configurations"

SITE_URL = "https://kort0881.github.io/internet-access-site/"

def fetch_news():
    """Парсит новости с Хабра (раздел Интернет) по ключевым словам."""
    news = []
    habr_url = 'https://habr.com/ru/rss/hub/internet/all/?fl=ru'
    keywords = ['доступ', 'интернет', 'связь', 'сеть', 'запрет', 'ограничени', 'регулирован']
    try:
        feed = feedparser.parse(habr_url)
        for entry in feed.entries[:10]:
            title_lower = entry.title.lower()
            if any(kw in title_lower for kw in keywords):
                summary = entry.summary
                if len(summary) > 300:
                    summary = summary[:300] + '...'
                news.append({
                    'title': entry.title,
                    'summary': summary,
                    'link': entry.link,
                    'date': datetime(*entry.published_parsed[:6]).strftime('%d %B %Y'),
                    'source': 'Хабр'
                })
    except Exception as e:
        print(f"⚠️ Ошибка парсинга новостей: {e}")

    if not news:
        news.append({
            'title': 'Актуальные новости о свободном доступе в сеть',
            'summary': 'Следите за новостями о регулировании интернета и доступе к сети.',
            'link': SITE_URL,
            'date': datetime.now().strftime('%d %B %Y'),
            'source': 'Новости'
        })
    return news

def clean_dist():
    """Очистка папки dist."""
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    print(f"✅ Папка {DIST_DIR} очищена")

def copy_static():
    """Копирование статических файлов."""
    if STATIC_DIR.exists():
        dest = DIST_DIR / 'static'
        shutil.copytree(STATIC_DIR, dest, dirs_exist_ok=True)
        print(f"✅ Статические файлы скопированы")

def copy_og_image():
    """Копирование og-image.png в dist."""
    src = Path('og-image.png')
    if src.exists():
        dest = DIST_DIR / 'og-image.png'
        shutil.copy2(src, dest)
        print(f"✅ OG image скопирован: {dest}")
    else:
        print("⚠️ OG image og-image.png не найден в корне репозитория")

def copy_favicons():
    """Копирование фавиконок в dist."""
    favicons = ['favicon.ico', 'favicon.png', 'favicon-96x96.png', 'apple-touch-icon.png']
    copied = 0
    for f in favicons:
        src = Path(f)
        if src.exists():
            dest = DIST_DIR / f
            shutil.copy2(src, dest)
            copied += 1
            print(f"✅ Скопирован: {f}")
    if copied == 0:
        print("⚠️ Фавиконки не найдены в корне репозитория")

def build_html():
    """Генерация HTML из шаблонов (RU + EN)."""
    print("\n🛠️ Сборка HTML...")

    print("📥 Загрузка конфигураций...")
    configs = get_vpn_configs()
    last_update = get_last_update_time()

    print("📰 Загрузка новостей...")
    news = fetch_news()

    print(f"✅ Найдено конфигураций: {len(configs)}")
    print(f"✅ Загружено новостей: {len(news)}")
    if last_update:
        print(f"⏰ Последнее обновление: {last_update}")

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))

    # --- RU (корень) ---
    template_ru = env.get_template('index.html')
    html_ru = template_ru.render(
        configs=configs,
        last_update=last_update,
        news=news,
        site_url=SITE_URL,
        meta_title=META_TITLE,
        meta_description=META_DESCRIPTION,
        meta_keywords=META_KEYWORDS,
        lang='ru',
    )
    (DIST_DIR / 'index.html').write_text(html_ru, encoding='utf-8')
    print(f"✅ Создан: {DIST_DIR / 'index.html'}")

    # --- EN (папка en/) ---
    en_dir = DIST_DIR / 'en'
    en_dir.mkdir(parents=True, exist_ok=True)
    template_en = env.get_template('index_en.html')
    html_en = template_en.render(
        configs=configs,
        last_update=last_update,
        news=news,
        site_url=SITE_URL,
        meta_title=META_TITLE_EN,
        meta_description=META_DESCRIPTION_EN,
        meta_keywords=META_KEYWORDS_EN,
        lang='en',
    )
    (en_dir / 'index.html').write_text(html_en, encoding='utf-8')
    print(f"✅ Создан: {en_dir / 'index.html'}")

def create_404():
    """Создание 404 страницы."""
    html_404 = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Страница не найдена</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen flex items-center justify-center">
    <div class="text-center">
        <h1 class="text-6xl font-bold text-indigo-600 mb-4">404</h1>
        <p class="text-2xl text-gray-700 mb-8">Страница не найдена</p>
        <a href="/internet-access-site/" class="bg-indigo-500 hover:bg-indigo-600 text-white px-6 py-3 rounded-lg inline-block transition">
            Вернуться на главную
        </a>
    </div>
</body>
</html>'''

    output_file = DIST_DIR / '404.html'
    output_file.write_text(html_404, encoding='utf-8')
    print(f"✅ Создан: {output_file}")

def create_robots_txt():
    """Создание robots.txt."""
    robots = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}sitemap.xml
"""
    output_file = DIST_DIR / 'robots.txt'
    output_file.write_text(robots, encoding='utf-8')
    print(f"✅ Создан: {output_file}")

def create_sitemap():
    """Создание sitemap.xml с обеими языковыми версиями."""
    today = datetime.now().strftime('%Y-%m-%d')

    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{SITE_URL}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>hourly</changefreq>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="ru" href="{SITE_URL}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE_URL}"/>
  </url>
  <url>
    <loc>{SITE_URL}en/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>hourly</changefreq>
    <priority>0.9</priority>
    <xhtml:link rel="alternate" hreflang="ru" href="{SITE_URL}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE_URL}"/>
  </url>
</urlset>
'''
    output_file = DIST_DIR / 'sitemap.xml'
    output_file.write_text(sitemap, encoding='utf-8')
    print(f"✅ Создан: {output_file}")

def main():
    """Основной процесс сборки."""
    print("🚀 Запуск сборки статического сайта...\n")

    clean_dist()
    copy_static()
    copy_og_image()
    copy_favicons()
    build_html()
    create_404()
    create_robots_txt()
    create_sitemap()

    print(f"\n✅ Сборка завершена! Результат в папке: {DIST_DIR}")
    print(f"🌐 Сайт будет доступен по адресу: {SITE_URL}")

if __name__ == '__main__':
    main()
