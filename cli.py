from argparse import ArgumentParser
from smtp import connect_smtp_from_config, create_message_from_yaml


# Set up arg parser for CLI args.
parser = ArgumentParser(description='Low water level detector.')
parser.add_argument('--email-to', '-to', required=True,
                    help='Send low water level alerts to this email.')
parser.add_argument('--smtp-key', '-k', required=True,
                    help='Path to SMTP key file on disk.')
parser.add_argument('--message-path', '-m', required=True,
                    help='Path to email message YAML file.')
parser.add_argument('--smtp-debug', action='store_true',
                    help=('Print full SMTP conversation with server. '
                          'Useful for debugging.'))
parser.add_argument('--verbose', '-v', action='store_true',
                    help='Print current action to terminal.')
args = parser.parse_args()


def info(msg):
    if args.verbose:
        print(msg)


# Connect to SMTP server.
info('Connect to SMTP server.')
s, username = connect_smtp_from_config(args.smtp_key,
                                       debug=args.smtp_debug)


# Create email message.
info('Load email message contents from disk.')
msg = create_message_from_yaml(to_addr=args.email_to,
                               from_addr=username,
                               path=args.message_path)
# msg = create_message(EMAIL_TO, username, subject, body)


info('Send email message.')
s.send_message(msg)
# s.sendmail(smtp_user, to, msg.as_string())

info('Close SMTP connection.')
s.quit()
