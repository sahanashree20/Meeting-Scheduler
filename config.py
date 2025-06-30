class Config:
    SECRET_KEY = "supersecretkey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/scheduler.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email config (optional)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'your_email@gmail.com'        # Replace with your email
    MAIL_PASSWORD = 'your_app_password_here'      # App password only!
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
