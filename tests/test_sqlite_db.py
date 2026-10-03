import unittest
from sqlite_db import initialize_database, insert_barcode, check_barcode
from config import DATABASE_PATH

class TestSQLiteDB(unittest.TestCase):
    def setUp(self):
        # Set up test environment
        pass

    def test_initialize_database(self):
        initialize_database()
        # Add assertions to verify that database is initialized correctly

    def test_insert_barcode(self):
        barcode_hash = 'some_barcode_hash'
        barcode = '123456789012'
        insert_barcode(barcode_hash, barcode)
        result = check_barcode(barcode_hash)
        self.assertEqual(result[0], barcode)  # Check that barcode is inserted and found

if __name__ == '__main__':
    unittest.main()