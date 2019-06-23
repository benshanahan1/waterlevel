# waterlevel

Alert when water drops below a certain level.


# set up email
* Create a new email address. [Yahoo Mail](https://mail.yahoo.com/) is recommended since Gmail is painful to get working.
* Go to [Yahoo Account Security settings](https://login.yahoo.com/account/security) > Account Security and set up 2-step verification.
* Create a new app password.
* Create a new key-file to store the username and password: `cp key/smtp.key.template key/smtp.key`
* Set `EMAIL_TO` environment variable so that script knows who to send email to.


# install
Install RPi Python library for Python 3:
```bash
sudo apt-get update
sudo apt-get -y install python3-rpi.gpio
```

Install Python requirements from file:
```bash
sudo pip3 install -r requirements.txt
```


## creating a key file
See 'key/email.key.template' for reference. The final file should be renamed to end in the 'key' extension so that it is not version-controlled.

```yml
# e.g. key/email.key
server: smtp.mail.yahoo.com
port: 587
username: fake_username
password: fake_password
```


## configuration
The following configuration options are available:

```txt
VARIABLE       DEFAULT
-------------------------------
SMTP_KEY       ./key/smtp.key
SMTP_DEBUG     False
EMAIL_TO       ''
MESSAGE_PATH   ./mail.yml
```

You can set any of these variables by defining them as environment variables. Use the `export` command to do so:

```bash
export EMAIL_TO='bob@gmail.com'
```


## creating a message
See 'mail.yml' for reference. The message should be a YAML file in the format:

```yml
# e.g. mail.yml
subject: The subject goes here
body: >
    The body content goes here.
    It can be split across multiple lines if you want.
```

## install crontab
Example crontab to run script once per hour:
```cron
0 * * * * SMTP_KEY=/home/pi/waterlevel/key/smtp.key MESSAGE_PATH=/home/pi/waterlevel/mail.yml EMAIL_TO=alice@gmail.com /usr/bin/python3 /home/pi/waterlevel/main.py
```
