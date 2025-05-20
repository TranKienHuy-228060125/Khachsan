import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost\\MSSQLSERVER02;'
        'DATABASE=HotelDB;'  # <-- bạn tạo DB tên này trước
        'Trusted_Connection=yes;'
    )
    return conn
