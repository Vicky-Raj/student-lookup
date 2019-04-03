from django.core.management.base import BaseCommand
from home.models import Student
from django.contrib.auth.models import User
import pandas as pd


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for student in Student.objects.all():
            student.user.delete()