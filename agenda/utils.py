from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from contracts.models import Contract


# class Calendar(HTMLCalendar):
#     def __init__(self, year=None, month=None):
#         self.year = year
#         self.month = month
#         super(Calendar, self).__init__()
#
#     # formats a day as a td
#     # filter events by day
#     def formatday(self, day, events):
#         events_per_day = events.filter(start_time__day=day)
#         d = ''
#         for event in events_per_day:
#             d += f"<li class='calendar-li'> {event.title} </li>"
#
#         if day != 0:
#             return f"<td class='calendar-td'><span class='date'>{day}</span><ul class='calendar-ul'> {d} </ul></td>"
#         return "<td class='calendar-td'></td>"
#
#     # formats a week as a tr
#     def formatweek(self, theweek, events):
#         week = ''
#         for d, weekday in theweek:
#             week += self.formatday(d, events)
#         return f"<tr class='calendar-tr'> {week} </tr>"
#
#     # formats a month as a table
#     # filter events by year and month
#     def formatmonth(self, withyear=True):
#         events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
#
#         cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
#         cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
#         cal += f'{self.formatweekheader()}\n'
#         for week in self.monthdays2calendar(self.year, self.month):
#             cal += f'{self.formatweek(week, events)}\n'
#         return cal

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
                d += f"<li class='calendar-li starting'>{contract.get_html_url} {contract.contract_name}</li>"
        for contract in contracts_ending_per_day:
                d += f"<li class='calendar-li ending'> {contract.contract_name} </li>"
        for contract in contracts_paying_per_day:
                d += f"<li class='calendar-li paying'> {contract.contract_name} </li>"


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
    def formatmonth(self, withyear=True):
        contracts = Contract.objects.filter(starting_date__year=self.year, starting_date__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, contracts)}\n'
        return cal