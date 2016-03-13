from django.core.management.base import BaseCommand
from MyTextSummarizer.models import Word


class Command(BaseCommand):
    help = 'Delete the Statement objects from database'

    def handle(self, *args, **options):
        Word.objects.all().delete()
        pass
