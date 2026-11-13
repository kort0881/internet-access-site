# 🌐 ДОСТУП К ИНТЕРНЕТУ

### Приватные VLESS Reality, Hysteria2 и Trojan подписки в Telegram · Бесплатные конфигурации на сайте

[![Telegram Bot](https://img.shields.io/badge/Telegram-@vlessbots__bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/vlessbots_bot)
[![Website](https://img.shields.io/badge/Website-Доступ-blue?style=for-the-badge&logo=firefox)](https://kort0881.github.io/internet-access-site/)
[![Telegram Channel](https://img.shields.io/badge/Telegram-@vlesstrojan-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/vlesstrojan)
[![GitHub stars](https://img.shields.io/github/stars/kort0881/internet-access-site?style=for-the-badge)](https://github.com/kort0881/internet-access-site/stargazers)
![GitHub issues](https://img.shields.io/github/issues/kort0881/internet-access-site?style=for-the-badge)

</div>

---

## 📝 О сервисе «ДОСТУП К ИНТЕРНЕТУ»

**«ДОСТУП К ИНТЕРНЕТУ»** — это платный Telegram-бот
[**@vlessbots_bot**](https://t.me/vlessbots_bot), который выдаёт **приватные высокоскоростные подписки**
на современных протоколах **VLESS Reality, Hysteria2 и Trojan**.

Сервис использует выделенные серверы без перегрузок, обеспечивает **высокую скорость для 4K-видео и онлайн-игр**,
**низкий пинг**, **шифрование трафика** и **защиту данных в публичных Wi-Fi**, а также **персональную поддержку** прямо в боте.

> 🚀 **Купить или продлить подписку:** [https://t.me/vlessbots_bot](https://t.me/vlessbots_bot)

Этот репозиторий — **официальный сайт-витрина** сервиса «ДОСТУП К ИНТЕРНЕТУ». На нём:

- 📡 **Бесплатные публичные конфигурации** VLESS, V2Ray, Hysteria, Trojan — обновляются каждый час из [vpn-checker-backend](https://github.com/kort0881/vpn-checker-backend).
- 🔌 **MTProto-прокси** для Telegram (Россия, Европа, США, Азия).
- 🧭 **Пошаговая инструкция** по подключению (Happ, Karing, v2rayNG, Hiddify, Streisand) — [раздел «Инструкция»](https://kort0881.github.io/internet-access-site/#howto).
- 📱 **Ссылки на клиенты** для Android, Windows, iOS / macOS.
- 📰 **Новости** о регулировании интернета и цифровой безопасности.
- 🤖 **`llms.txt`** — структурированное описание для ИИ-краулеров (ChatGPT, Claude, Perplexity).

Бесплатные конфигурации — это способ познакомиться с протоколами и клиентами.
Для стабильной ежедневной работы выбирайте **приватную подписку** в боте
[**@vlessbots_bot**](https://t.me/vlessbots_bot): выделенные серверы, высокая скорость, низкий пинг и поддержка.

---

## ⚖️ Бесплатно на сайте vs Платно в @vlessbots_bot

| Возможность | Бесплатно на сайте | Платно в @vlessbots_bot |
|---|---|---|
| Серверы | Публичные, общие | **Выделенные, приватные** |
| Стабильность | Возможны перегрузки | **Без перегрузок** |
| Скорость | Не гарантируется | **4K-видео, онлайн-игры** |
| Пинг | Зависит от нагрузки | **Низкий и стабильный** |
| Протоколы | VLESS, V2Ray, Hysteria, Trojan | **VLESS Reality, Hysteria2, Trojan** |
| Шифрование | Базовое | **Современное, с защитой в публичных Wi-Fi** |
| Поддержка | — | **Персональная в боте** |
| Обновление ключей | Автоматическое | Автоматическое в Telegram |
| Оплата и продление | — | **Прямо в боте** |
| Тестовый период | — | **2 дня бесплатно** |

---

## 🚀 Быстрый старт (для разработчиков)

### Установка

```bash
# 1. Клонирование репозитория
git clone https://github.com/kort0881/internet-access-site.git
cd internet-access-site

# 2. Создание виртуального окружения
python -m venv .env

# Windows:
.env\Scripts\activate

# Linux/macOS:
source .env/bin/activate

# 3. Установка зависимостей
pip install -r requirements.txt
Запуск
bash
# Локальный сервер (Flask)
python main.py

# Сайт будет доступен по адресу: http://127.0.0.1:5000
Статическая сборка для GitHub Pages
bash
# Сгенерировать статический сайт (RU + EN + llms.txt + robots.txt + sitemap.xml)
python build.py

# Результат будет в папке dist/
🛠️ Технологии
Backend: Python 3.10+, Flask, Waitress

Генератор статики: Jinja2 + build.py

Frontend: HTML5, TailwindCSS, Alpine.js, FontAwesome, Geist (шрифт)

CI/CD: GitHub Actions (сборка и деплой каждый час)

Источник данных: vpn-checker-backend

SEO / GEO: Schema.org JSON-LD (WebSite, HowTo, FAQPage), sitemap.xml, robots.txt, llms.txt

📱 Поддерживаемые клиенты
Android: v2rayNG, NekoBox, Happ, Karing, Hiddify

Windows: v2rayN, Hiddify

iOS / macOS: Shadowrocket, Streisand, Happ

Универсальные: Hiddify (все платформы)

Формат ссылки на подписку — стандартный, импортируется в клиент одним нажатием.
Подробная инструкция — на сайте: https://kort0881.github.io/internet-access-site/#howto

💬 Telegram
🤖 Платный бот (приватные подписки): @vlessbots_bot

📢 Информационный канал: @vlesstrojan

💬 KiberSOS: @kibersosnew

👥 Чат «Доступ к интернету»: присоединиться

💻 Структура проекта
text
internet-access-site/
├── main.py                  # Flask приложение (локальная разработка)
├── services.py              # Парсер конфигураций из vpn-checker-backend
├── build.py                 # Генератор статики (RU + EN + llms.txt + robots + sitemap)
├── fetch_telegram_news.py   # Посты из Telegram-канала @vlesstrojan → telegram_news.json
├── telegram_news.json       # Кэш новостей (генерируется автоматически, в git не попадает)
├── requirements.txt         # Python зависимости
├── llms.txt                 # Описание для ИИ-краулеров (ChatGPT, Claude, Perplexity)
├── templates/
│   ├── index.html           # Шаблон RU (с секцией #howto и JSON-LD)
│   └── index_en.html        # Шаблон EN (с секцией #howto и JSON-LD)
├── static/
│   └── background.gif       # Фон hero-секции
├── favicon.ico / favicon.png
├── og-image.png             # Open Graph превью
└── .github/
    └── workflows/
        └── deploy.yml       # Автоматический деплой на GitHub Pages
⚙️ Настройка GitHub Pages
Перейдите в Settings → Pages

В Source выберите gh-pages branch (или настройте деплой через Actions)

Сайт будет доступен по адресу: https://kort0881.github.io/internet-access-site/

Что публикуется автоматически
index.html — русская версия (с #howto и JSON-LD WebSite + HowTo + FAQPage)

en/index.html — английская версия

llms.txt — описание для LLM-краулеров

robots.txt — с разрешением для GPTBot, ClaudeBot, PerplexityBot, Google-Extended

sitemap.xml — с hreflang для RU / EN

404.html — страница ошибки

🔄 Автоматизация
GitHub Actions автоматически:

✅ Собирает сайт каждый час

✅ Обновляет конфигурации из vpn-checker-backend

✅ Дублирует посты Telegram-канала @vlesstrojan в блок «Новости» (публичная лента t.me/s/, без api_id/api_hash)

✅ Копирует llms.txt в dist/

✅ Генерирует robots.txt с правилами для LLM-ботов

✅ Генерирует sitemap.xml с обеими языковыми версиями

✅ Деплоит на GitHub Pages

🔍 SEO и видимость в LLM
Сайт оптимизирован для поисковых систем и языковых моделей:

Schema.org JSON-LD: WebSite, HowTo, FAQPage — помогают Google, Яндексу и нейросетям напрямую парсить инструкцию и ответы на вопросы.

Статичный текст: инструкция и FAQ находятся в HTML-коде страницы (не подгружаются через JS), поэтому доступны краулерам.

llms.txt: структурированное описание бренда, возможностей и ссылок — по стандарту для ИИ-краулеров.

robots.txt: явно разрешает индексацию GPTBot, ClaudeBot, PerplexityBot, Google-Extended.

hreflang: корректная связка RU и EN версий.

📝 Лицензия
MIT License — свободно используйте и изменяйте!

<div align="center">
⭐ Поставьте звезду, если проект полезен!

🌐 Открыть сайт · 🤖 Открыть @vlessbots_bot · 📢 Telegram-канал · 🐛 Issues

</div> ```
