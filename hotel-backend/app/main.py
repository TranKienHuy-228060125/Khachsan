from fastapi import FastAPI
import pyodbc

app = FastAPI()

# ⚙️ Cấu hình kết nối SQL Server
def get_db_connection():
    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=localhost\MSSQLSERVER02;'
        r'DATABASE=KHACHSAN;' 
        r'Trusted_Connection=yes;'
    )
    return conn

# ✅ Kiểm tra API chạy
@app.get("/")
def read_root():
    return {"message": "API is running!"}

# 🏨 Lấy danh sách phòng từ bảng Rooms
@app.get("/rooms")
def get_rooms():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT RoomID, RoomName, Price FROM Rooms")
    rows = cursor.fetchall()
    conn.close()
    return [
        {"id": row.RoomID, "name": row.RoomName, "price": float(row.Price)}
        for row in rows
    ]
