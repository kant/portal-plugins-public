from django.core.management.base import BaseCommand, CommandError
from portal.plugins.gnmgridintegration.management.management_mixin import ManagementMixin

class Command(ManagementMixin, BaseCommand):
    help = 'Installs the Grid integrator plugin'

    def handle(self, *args, **options):
        self.setup_notification()

