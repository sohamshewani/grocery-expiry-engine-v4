import unittest
from barcode_hash import hash_barcode, check_barcode, insert_barcode
from config import DATABASE_PATH

class TestBarcodeHash(unittest.TestCase):
    def setUp(self):
        # Set up test environment
        pass

    def test_hash_barcode(self):
        barcode = '123456789012'
        barcode_hash = hash_barcode(barcode)
        self.assertEqual(len(barcode_hash), 64)  # Check that hash is 64 characters long

    def test_check_barcode(self):
        barcode_hash = 'some_barcode_hash'
        result = check_barcode(barcode_hash)
        self.assertIsNone(result)  # Check that barcode is not found

    def test_insert_barcode(self):
        barcode_hash = 'some_barcode_hash'
        barcode = '123456789012'
        insert_barcode(barcode_hash, barcode)
        result = check_barcode(barcode_hash)
        self.assertEqual(result[0], barcode)  # Check that barcode is inserted and found

if __name__ == '__main__':
    unittest.main()