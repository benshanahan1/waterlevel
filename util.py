from yaml import load, FullLoader
from pathlib import Path
from exceptions import NoServerError, NoCredentialsError


def load_smtp_config(path):
    """Load SMTP config from SMTP key file.

    :param str path: Path to SMTP key file.
    """
    abspath = Path(path).resolve()  # resolve absolute path
    with open(abspath, 'r') as fd:
        config = load(fd, Loader=FullLoader)
        server = config['server']
        port = int(config['port'])
        username = config['username']
        password = config['password']

    # Check if username and password were provided.
    if not server or not port:
        raise NoServerError('SMTP server address and/or port not set.')

    if not username or not password:
        raise NoCredentialsError('SMTP username and/or password not set.')

    return server, port, username, password
