import os

# Configuration settings
OCR_CONFIG = {
    'language': 'eng',
    'config': '--psm 6',
}

DATABASE_PATH = os.path.join(os.getcwd(), 'grocery.db')