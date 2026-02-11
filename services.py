import requests
import re
from datetime import datetime, timedelta

# Кэш для данных
CONFIGS_CACHE = None
CONFIGS_CACHE_TIME = None
CACHE_DURATION = timedelta(minutes=30)

def parse_subscriptions_list():
    """Парсит список подписок из vpn-checker-backend"""
    try:
        response = requests.get(
            'https://raw.githubusercontent.com/kort0881/vpn-checker-backend/main/checked/subscriptions_list.txt',
            timeout=10
        )
        if response.status_code != 200:
            return []
        
        content = response.text
        configs = []
        
        # Парсим категории
        current_category = None
        for line in content.split('\n'):
            line = line.strip()
            
            # Определяем категорию
            if line.startswith('===') and '===' in line:
                # Извлекаем название категории
                category_match = re.search(r'===\s*(.+?)\s*===', line)
                if category_match:
                    current_category = category_match.group(1)
                continue
            
            # Если это ссылка на конфиг
            if line.startswith('https://'):
                # Извлекаем имя файла из URL
                filename = line.split('/')[-1]
                
                configs.append({
                    'url': line,
                    'name': filename.replace('.txt', ''),
                    'category': current_category or 'Общие',
                    'filename': filename
                })
        
        return configs
    except Exception as e:
        print(f"Ошибка при парсинге subscriptions_list.txt: {e}")
        return []

def get_vpn_configs():
    """Получить все VPN конфигурации с кэшированием"""
    global CONFIGS_CACHE, CONFIGS_CACHE_TIME
    
    # Проверяем кэш
    if CONFIGS_CACHE and CONFIGS_CACHE_TIME:
        if datetime.now() - CONFIGS_CACHE_TIME < CACHE_DURATION:
            return CONFIGS_CACHE
    
    # Получаем список подписок
    subscriptions = parse_subscriptions_list()
    
    configs = []
    for idx, sub in enumerate(subscriptions, 1):
        config = {
            "id": idx,
            "name": sub['name'],
            "url": sub['url'],
            "category": sub['category'],
            "is_recommended": 'white' in sub['filename'].lower(),  # Помечаем white конфиги как рекомендованные
        }
        configs.append(config)
    
    # Кэшируем результат
    CONFIGS_CACHE = configs
    CONFIGS_CACHE_TIME = datetime.now()
    
    return configs

def get_last_update_time():
    """Получить время последнего обновления репозитория"""
    try:
        response = requests.get(
            'https://api.github.com/repos/kort0881/vpn-checker-backend/commits/main',
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            commit_date = data.get('commit', {}).get('committer', {}).get('date')
            if commit_date:
                # Конвертируем в читаемый формат
                dt = datetime.fromisoformat(commit_date.replace('Z', '+00:00'))
                return dt.strftime('%d.%m.%Y %H:%M')
    except Exception as e:
        print(f"Ошибка при получении времени обновления: {e}")
    return None
