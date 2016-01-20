from django.core.management.base import BaseCommand

from myproject.myapp.management.pcag import generate_usecase


class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        generate_usecase('teste')
        self.stdout.write('Usecase gerado: teste_usecase.py\n')
