from connect import get_connection

try:
    conn = get_connection()
    print("✅ Подключение успешно!")
    conn.close()
except Exception as e:
    print("❌ Ошибка подключения:", e)