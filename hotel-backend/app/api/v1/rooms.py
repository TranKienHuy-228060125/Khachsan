from app.core.database import get_connection

def get_all_rooms():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT RoomID, RoomName, Price FROM Rooms")
    rows = cursor.fetchall()
    conn.close()
    return rows
