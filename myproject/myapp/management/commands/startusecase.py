from django.core.management.base import BaseCommand

from myproject.myapp.management.pcag import generate_usecase


class Command(BaseCommand):
    args = 'usecase_name'
    help = 'Generates a usecase class'

    def handle(self, *args, **options):
        name = args[0]

        generated_usecase = generate_usecase(name)
        self.stdout.write('Generated Usecase: {0}\n'.format(generated_usecase))
