from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    birthday_month = 11  # November
    birthday_day = 1  # 1st

    today = datetime.date.today()
    birthday_this_year = datetime.date(today.year, birthday_month, birthday_day)

    if today > birthday_this_year:
        birthday_this_year = datetime.date(today.year + 1, birthday_month, birthday_day)

    time_to_birthday = birthday_this_year - today

    return render(request, "bday/index.html", {
        "mybday": now.month == birthday_month and now.day == birthday_day,
        "days_until_birthday": time_to_birthday.days,
        
    })