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
python cli.py -k /path/to/email.key -to benshanahan1@gmail.com
```

For SMTP debugging, add flag `--smtp-debug`. For general verbose output, add flag `--verbose`.
