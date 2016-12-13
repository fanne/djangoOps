from __future__ import unicode_literals

from django.apps import AppConfig


class OwgameConfig(AppConfig):
    name = 'owgame'

    def ready(self):
        import owgame.signals
        import owgame.owgame_ansible_host

