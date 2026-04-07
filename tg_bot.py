import requests

token = "8730457637:AAGx_t8WgdJrBSRcmBD9q05MNjCM2pbFs3c"
url = f"https://api.telegram.org/bot{token}/getUpdates"

response = requests.get(url)
data = response.json()

if data["ok"] and data["result"]:
    # Берем последнее обновление
    last_update = data["result"][-1]
    
    # Извлекаем chat_id
    chat_id = last_update["message"]["chat"]["id"]
    chat_type = last_update["message"]["chat"]["type"]
    chat_title = last_update["message"]["chat"].get("title", "Личный чат")
    
    print(f"✅ Chat ID: {chat_id}")
    print(f"📌 Тип чата: {chat_type}")
    print(f"📝 Название: {chat_title}")
    
    # Дополнительная информация
    if "first_name" in last_update["message"]["chat"]:
        print(f"👤 Имя: {last_update['message']['chat']['first_name']}")
else:
    print("❌ Нет новых сообщений. Отправьте что-нибудь боту!")