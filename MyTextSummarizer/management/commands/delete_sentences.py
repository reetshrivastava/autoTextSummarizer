from django.core.management.base import BaseCommand
from MyTextSummarizer.models import Sentance


class Command(BaseCommand):
    help = 'Delete the Statement objects from database'

    def handle(self, *args, **options):
        Sentance.objects.all().delete()
        pass
