import smtplib
from os import environ
from email.message import EmailMessage
from json import load


key_path = environ.get('EMAIL_KEY', './yahoo.key')
to = environ.get('TO_ADDR', 'benshanahan1@gmail.com')
server = environ.get('SMTP_SERVER', 'smtp.mail.yahoo.com')
port = environ.get('SMTP_PORT', 587)

debug_mode = False


class NoCredentialsError(Exception):
    pass


# Load credentials.
with open(key_path, 'r') as fd:
    creds = load(fd)
    smtp_user = creds['username']
    smtp_pswd = creds['password']


if not smtp_user or not smtp_pswd:
    raise NoCredentialsError('SMTP username and/or password not set.')


msg = EmailMessage()
msg.set_content('Detected low water level.')
msg['Subject'] = 'Check water level'
msg['From'] = smtp_user
msg['To'] = to


s = smtplib.SMTP(server, port, timeout=10)
if debug_mode:
    s.set_debuglevel(1)
s.ehlo()
s.starttls()
s.login(smtp_user, smtp_pswd)

print('sending email')
s.send_message(msg)
# s.sendmail(smtp_user, to, msg.as_string())
s.quit()
