import os

class Config:
    # Secret key for sessions and security
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-saree-factory-secret-key-987123654')
    
    # Base directory of the application
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # SQLite Database location inside workspace, with easy switch to MySQL
    # To use MySQL: set environment variable DATABASE_URL=mysql+pymysql://username:password@localhost/db_name
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 
        f"sqlite:///{os.path.join(BASE_DIR, 'saree_factory.db')}"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Folder to store generated PDF invoices
    PDF_FOLDER = os.path.join(BASE_DIR, 'app', 'static', 'invoices')
    
    # Ensure PDF upload/invoice directory exists
    os.makedirs(PDF_FOLDER, exist_ok=True)
