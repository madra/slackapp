from django.core.management.base import BaseCommand

from slack_app import SlackApp


class Command(BaseCommand):

    def handle(self, **options):
        """
        Send test message to slack
        :param options:
        :return:
        """
        slack_app = SlackApp()

        slack_app.send_message(message='sente: Test message')
