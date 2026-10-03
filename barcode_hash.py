import hashlib
from config import DATABASE_PATH

# Hash function for barcodes
def hash_barcode(barcode):
    hash_object = hashlib.sha256(barcode.encode())
    return hash_object.hexdigest()

# Check for existing barcode in database
def check_barcode(barcode_hash):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT barcode FROM barcodes WHERE hash=?", (barcode_hash,))
    result = cursor.fetchone()
    connection.close()
    return result

# Insert barcode into database
def insert_barcode(barcode_hash, barcode):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO barcodes (hash, barcode) VALUES (?, ?)", (barcode_hash, barcode))
    connection.commit()
    connection.close()
