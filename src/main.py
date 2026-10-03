import ocr
import barcode_hash
import sqlite_db
import expiry_forecaster
def run_application():
    ocr_data = ocr.process_ocr_data()
    barcodes = [barcode_hash.get_barcode_hash(barcode) for barcode in ocr_data]
    for barcode_hash in barcodes:
        expiry_date = expiry_forecaster.forecast_expiry_date(barcode_hash)
        sqlite_db.store_expiry_dates(barcode_hash, expiry_date)