from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from contracts.models import Contract



class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        contracts_starting_per_day = events.filter(starting_date__day=day)
        contracts_ending_per_day = events.filter(ending_date__day=day)
        contracts_paying_per_day = events.filter(payment_date__day=day)
        d = ''

        for contract in contracts_starting_per_day:
            if contract.company_client:
                client = contract.company_client
            elif contract.person_client:
                client = contract.person_client
            else:
                client = '-'
            d += f"<a href='http://127.0.0.1:8000/contracts/editct/{contract.id}'> <li class='calendar-li starting' title='{contract.contract_name}'> {contract.contract_name}  <p class='calendar-p'> {client} </p> </li> </a>"
        for contract in contracts_ending_per_day:
            if contract.company_client:
                client = contract.company_client
            elif contract.person_client:
                client = contract.person_client
            else:
                client = '-'
            d += f"<a href='http://127.0.0.1:8000/contracts/editct/{contract.id}'> <li class='calendar-li ending' title='{contract.contract_name}'> {contract.contract_name} <p class='calendar-p'> {client} </p> </li> </a>"
        for contract in contracts_paying_per_day:
            if contract.company_client:
                client = contract.company_client
            elif contract.person_client:
                client = contract.person_client
            else:
                client = '-'
            d += f"<a href='http://127.0.0.1:8000/contracts/editct/{contract.id}'> <li class='calendar-li paying' title='{contract.contract_name}'> {contract.contract_name} <p class='calendar-p'> {client} </p> </li> </a>"



        if day != 0:
            return f"<td class='calendar-td'><span class='date'>{day}</span><ul class='calendar-ul'> {d} </ul></td>"
        return "<td class='calendar-td'></td>"

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f"<tr class='calendar-tr'> {week} </tr>"

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True, contracts=None):
        contracts = contracts.filter(starting_date__year=self.year, starting_date__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, contracts)}\n'
        return cal
