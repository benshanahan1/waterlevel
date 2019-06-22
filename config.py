from os import environ


SMTP_KEY = environ.get('SMTP_KEY', './key/smtp.key')
SMTP_DEBUG = environ.get('SMTP_DEBUG', False)
EMAIL_TO = environ.get('EMAIL_TO', '')
MESSAGE_PATH = environ.get('MESSAGE_PATH', './mail.yml')
