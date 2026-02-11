from flask import Flask, render_template, send_from_directory, jsonify, Response
from services import get_vpn_configs, get_last_update_time
import requests
import json
import os
from datetime import datetime, timedelta
from urllib.parse import urljoin

app = Flask(__name__)

# SEO defaults
DEFAULT_META_TITLE = "Доступ к интернету - Бесплатные VPN конфигурации"
DEFAULT_META_DESCRIPTION = (
    "Автоматические VPN-конфиги для V2Ray, VLESS, Hysteria, Trojan, VMess, Reality и Shadowsocks. "
    "Регулярное обновление, удобные ссылки. Подписывайтесь на Telegram!"
)
DEFAULT_META_KEYWORDS = "vpn, vless, v2ray, shadowsocks, hysteria, trojan, vmess, reality, vpn configs, free vpn, доступ к интернету, обход блокировок"

# Кэш для ссылок на скачивание
CACHE_FILE = 'download_links_cache.json'
CACHE_DURATION = timedelta(hours=24)

# Fallback ссылки
FALLBACK_LINKS = {
    'v2rayng-apk': 'https://github.com/2dust/v2rayNG/releases/latest',
    'nekobox-apk': 'https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/latest',
    'v2rayn-win': 'https://github.com/2dust/v2rayN/releases/latest',
}

def normalize_site_url(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    if not value:
        return None
    if not value.endswith('/'):
        value += '/'
    return value

def get_site_url() -> str | None:
    site_url = normalize_site_url(os.environ.get('SITE_URL'))
    if site_url:
        return site_url
    try:
        from flask import request
        return normalize_site_url(request.url_root)
    except RuntimeError:
        return None

@app.route('/')
def home():
    configs = get_vpn_configs()
    last_update = get_last_update_time()
    site_url = get_site_url()
    
    return render_template(
        'index.html',
        configs=configs,
        last_update=last_update,
        site_url=site_url,
        meta_title=DEFAULT_META_TITLE,
        meta_description=DEFAULT_META_DESCRIPTION,
        meta_keywords=DEFAULT_META_KEYWORDS
    )

@app.route('/robots.txt')
def robots_txt():
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /api/\n"
    )
    return Response(content, mimetype='text/plain')

@app.route('/api/download-links')
def get_download_links():
    """API endpoint для получения ссылок на скачивание"""
    return jsonify(FALLBACK_LINKS)

@app.route('/api/github-stats')
def get_github_stats():
    """API endpoint для получения статистики репозитория"""
    repo = 'kort0881/vpn-checker-backend'
    try:
        response = requests.get(f'https://api.github.com/repos/{repo}', timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), getattr(e.response, 'status_code', 500)

if __name__ == '__main__':
    from waitress import serve
    print("🚀 Запуск сайта на http://127.0.0.1:5000")
    serve(app, host='127.0.0.1', port=5000)
