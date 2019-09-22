import requests
import logging

from django.conf import settings


logger = logging.getLogger('root')


class SlackApp(object):

    def __init__(self):
        self.webhook = settings.SLACK_INCOMING_WEBHOOK if\
            settings.SLACK_INCOMING_WEBHOOK else ''

    def send_message(self, message,
                     slack_channel=settings.SLACK_ERROR_CHANNEL):
        payload = {
            'text': message
        }

        if settings.SLACK_USERNAME:
            payload['username'] = settings.SLACK_USERNAME

        if slack_channel:
            payload['channel'] = settings.SLACK_CHANNEL

        if self.webhook:
            response = requests.post(
                self.webhook,
                json=payload,
                verify=False,
            )
            if response.status_code != 200:
                logger.error(
                    'Error sending slack report. Status code: {}. Response: {}'.format(
                        response.status_code,
                        response.text
                    ))
        else:
            logger.error(
                'There is no slack incoming webhook set in settings')

    def send_login_failure(self, username):
        # Build message from constant parts and method parameters
        message = '*Login failure*' \
                  '\nError while authenticating user: {}'.format(username)
        self.send_message(message)
