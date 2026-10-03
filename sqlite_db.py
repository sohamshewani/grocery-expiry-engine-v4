import sqlite3
from config import DATABASE_PATH

# Initialize database
def initialize_database():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS barcodes (hash TEXT PRIMARY KEY, barcode TEXT)")
    connection.commit()
    connection.close()

# Insert barcode into database
def insert_barcode(barcode_hash, barcode):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO barcodes (hash, barcode) VALUES (?, ?)", (barcode_hash, barcode))
    connection.commit()
    connection.close()

# Check for existing barcode in database
def check_barcode(barcode_hash):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT barcode FROM barcodes WHERE hash=?", (barcode_hash,))
    result = cursor.fetchone()
    connection.close()
    return result
