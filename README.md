# waterlevel

Alert when water drops below a certain level.



# set up email
* Create a new email address. [Yahoo Mail](https://mail.yahoo.com/) is recommended since Gmail is painful to get working.
* Go to [Yahoo Account Security settings](https://login.yahoo.com/account/security) > Account Security and set up 2-step verification.
* Create a new app password.
* Create a new key-file to store the username and password: `cp key/email.key.template key/email.key`


# install
...


# usage
Use the CLI:

```bash
python cli.py --help
python cli.py -k /path/to/email.key -to destination@gmail.com -m /path/to/mail.yml
```

For SMTP debugging, add flag `--smtp-debug`. For general verbose output, add flag `--verbose`.


## creating a key file
See 'key/email.key.template' for reference. The final file should be renamed to end in the 'key' extension so that it is not version-controlled.

```yml
# e.g. key/email.key
server: smtp.mail.yahoo.com
port: 587
username: fake_username
password: fake_password
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
