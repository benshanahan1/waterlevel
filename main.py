import os
import RPi.GPIO as GPIO
from config import SMTP_KEY, SMTP_DEBUG, EMAIL_TO, MESSAGE_PATH
from smtp import connect_smtp_from_config, create_message_from_yaml


SENSOR_PIN = 11
LOG_FILE = '/tmp/no-water'


def setup_gpio():
    """ Configure GPIO."""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SENSOR_PIN, GPIO.IN)


def read_sensor():
    """ Read value of GPIO pin. """
    return GPIO.input(SENSOR_PIN)


def touch(path):
    """ Touch empty file. """
    with open(path, 'w') as fd:
        fd.write('')


def send_email():
    s, username = connect_smtp_from_config(SMTP_KEY,
                                           debug=SMTP_DEBUG)
    msg = create_message_from_yaml(to_addr=EMAIL_TO,
                                   from_addr=username,
                                   path=MESSAGE_PATH)
    s.send_message(msg)


def handle_low_water():
    """ Low water level. """
    print('Detected low water level. Sending alert email.')
    send_email()
    touch(LOG_FILE)  # create file


def handle_sufficient_water():
    """ Sufficient water level. """
    print('Detected water.')
    try:
        os.remove(LOG_FILE)
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    # Setup and read from GPIO.
    setup_gpio()
    low_water = read_sensor()

    # Check if file exists.
    file_exists = os.path.isfile(LOG_FILE)
   
    # Is the water level low?
    if low_water and not file_exists:
        handle_low_water()

    # Is the water level sufficient?
    if not low_water:
        handle_sufficient_water()
