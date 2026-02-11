<div align="center">

# 🌐 Доступ к интернету

### Бесплатные VPN конфигурации для обхода блокировок

[![Website](https://img.shields.io/badge/Website-Доступ-blue?style=for-the-badge&logo=firefox)](https://kort0881.github.io/internet-access-site/)
[![GitHub stars](https://img.shields.io/github/stars/kort0881/internet-access-site?style=for-the-badge)](https://github.com/kort0881/internet-access-site/stargazers)
![GitHub issues](https://img.shields.io/github/issues/kort0881/internet-access-site?style=for-the-badge)

</div>

## 📝 Описание

Веб-сайт для автоматического парсинга и предоставления VPN-конфигураций из [vpn-checker-backend](https://github.com/kort0881/vpn-checker-backend).

### ✨ Возможности

- 🔄 **Автоматическое обновление**: Конфигурации парсятся из `subscriptions_list.txt`
- 🇷🇺 **Категории**: Россия, Европа и другие
- ⭐ **Рекомендации**: Автоматическое выделение `white` конфигураций
- 📱 **Современный UI**: Адаптивный дизайн с TailwindCSS
- 📢 **Telegram интеграция**: Прямые ссылки на каналы
- ⏰ **GitHub Actions**: Автоматическая сборка и деплой каждый час

## 🚀 Быстрый старт

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
```

### Запуск

```bash
# Локальный сервер
python main.py

# Сайт будет доступен по адресу: http://127.0.0.1:5000
```

### Статическая сборка

```bash
# Сгенерировать статический сайт для GitHub Pages
python build.py

# Результат будет в папке dist/
```

## 🛠️ Технологии

- **Backend**: Python 3.10+, Flask, Waitress
- **Frontend**: HTML5, TailwindCSS, Alpine.js, FontAwesome
- **CI/CD**: GitHub Actions
- **Источник данных**: [vpn-checker-backend](https://github.com/kort0881/vpn-checker-backend)

## 💬 Telegram каналы

- 🔗 [VLESS & Trojan](https://t.me/vlesstrojan)
- 🔗 [KiberSOS](https://t.me/kibersosnew)
- 🔗 [Доступ к интернету](https://t.me/+aukDHGFAhE41NWQy)

## 💻 Разработка

### Структура проекта

```
internet-access-site/
├── main.py              # Flask приложение
├── services.py          # Парсер конфигураций
├── build.py             # Скрипт сборки
├── requirements.txt     # Python зависимости
├── templates/
│   └── index.html       # Главный шаблон
└── .github/
    └── workflows/
        └── deploy.yml   # Автоматический деплой
```

## ⚙️ Настройка GitHub Pages

1. Перейдите в **Settings** → **Pages**
2. В **Source** выберите **gh-pages branch**
3. Сайт будет доступен по адресу: `https://kort0881.github.io/internet-access-site/`

## 🔄 Автоматизация

GitHub Actions автоматически:
- ✅ Собирает сайт каждый час
- ✅ Обновляет конфигурации из `vpn-checker-backend`
- ✅ Деплойт на GitHub Pages

## 📝 Лицензия

MIT License - свободно используйте и изменяйте!

---

<div align="center">

**⭐ Поставьте звезду, если проект полезен!**

[🌐 Открыть сайт](https://kort0881.github.io/internet-access-site/) | [📢 Telegram](https://t.me/vlesstrojan) | [🐛 Issues](https://github.com/kort0881/internet-access-site/issues)

</div>
