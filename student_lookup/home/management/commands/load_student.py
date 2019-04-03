from django.core.management.base import BaseCommand
from home.models import Student
from django.contrib.auth.models import User
import pandas as pd


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        sheet = pd.read_excel('home/sheets/CSE C.xlsx')
        i = 0
        while True:
            try:
                if sheet['roll no'][i] != sheet['roll no'][i]:
                    break
            except KeyError:
                break
            user = User()
            user.username = sheet['roll no'][i]
            user.first_name = sheet['name'][i]
            user.email = sheet['mail id'][i] + '@skct.edu.in'
            user.set_password('123testpass')
            user.save()
            student = Student()
            student.user = user
            student.reg_no = sheet['roll no'][i]
            student.dep = sheet['department'][i]
            student.room = sheet['room no'][i]
            student.batch = sheet['batch no'][i]
            student.parent_no = str(int(sheet['parents no'][i]))
            student.student_no = str(int(sheet['student no'][i]))
            student.image = f"/profile_img/{sheet['roll no'][i]}.jpg"
            student.save()
            print(sheet['roll no'][i])
            i += 1