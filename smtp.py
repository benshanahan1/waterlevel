from smtplib import SMTP
from yaml import load, FullLoader
from util import load_smtp_config
from email.message import EmailMessage


def connect_smtp_from_config(path, timeout=None, debug=False):
    """Connect to SMTP server from config file.

    :param str path: Config file path.
    :param int timeout: Timeout to connect to SMTP server. By default, timeout
        is disabled (set to 0). If timeout is specified and is reached without
        a SMTP connection being established, a `socket.timeout` exception is
        raised.
    :param bool debug: Show full SMTP conversation.
    :rtype: tuple
    :return: Tuple where first element is the connected SMTP server object and
        the second element is the SMTP username.
    """
    server, port, username, password = load_smtp_config(path)
    s = connect_smtp(server,
                     port,
                     username,
                     password,
                     timeout=timeout,
                     debug=debug)
    return s, username


def connect_smtp(server, port, username, password, timeout=None, debug=False):
    """Connect to SMTP server.

    :param str server: SMTP server address.
    :param int port: SMTP server port.
    :param str username: SMTP account username.
    :param str password: SMTP account password. Depending on the SMTP server
        security settings, this might need to be an app password instead of the
        actual account password.
    :param int timeout: Timeout to connect to SMTP server. By default, timeout
        is disabled (set to 0). If timeout is specified and is reached without
        a SMTP connection being established, a `socket.timeout` exception is
        raised.
    :param bool debug: Show full SMTP conversation.
    """
    s = SMTP(server, port, timeout=timeout)
    if debug:
        s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.login(username, password)
    return s


def create_message(to_addr, from_addr, subject, body):
    """Create an email message in the proper format.

    :param str to_addr: To email address.
    :param str from_addr: From email address.
    :param str subject: Email subject.
    :param str body: Email body.
    """
    msg = EmailMessage()
    msg['To'] = to_addr
    msg['From'] = from_addr
    msg['Subject'] = subject
    msg.set_content(body)
    return msg


def create_message_from_yaml(to_addr, from_addr, path):
    """Create an email message from a YAML file.

    :param str to_addr: To email address.
    :param str from_addr: From email address.
    :param str path: Path to YAML file.
    """
    with open(path, 'r') as fd:
        data = load(fd, Loader=FullLoader)
    msg = EmailMessage()
    msg['To'] = to_addr
    msg['From'] = from_addr
    msg['Subject'] = data['subject']
    msg.set_content(data['body'])
    return msg
