import calendar
from datetime import datetime, date, timedelta

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.views import generic
from django.utils.safestring import mark_safe
from django.views.generic import FormView

from contracts.models import Contract
from .forms import TaskForm
from .models import Task
from .utils import Calendar

from django.contrib.auth.mixins import LoginRequiredMixin

class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Contract
    template_name = 'calendar.html'

    # Send to calendar only the contracts that belongs to the user of the request
    def get_queryset(self):
        return Contract.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the actual month to display the calendar
        d = get_date(self.request.GET.get('month', None))
        agenda = Calendar(d.year, d.month)
        # Send the contracts to the Calendar
        html_agenda = agenda.formatmonth(withyear=True, contracts=self.get_queryset())
        context['calendar'] = mark_safe(html_agenda)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month





"""
ADD A NEW TOOD
"""
@login_required
def new_task(request):
    user = request.user
    form = TaskForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('person_list')
    return render(request, 'add_task.html', {'form': form})


"""
LIST THE CLIENT PERSONS
"""
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('completed')
    pending_tasks = Task.objects.filter(user=request.user).aggregate(sum=Sum('completed'!=True))['sum'] or 0
    return render(request, 'list_task.html', {'tasks': tasks,
                                                       'pending_tasks': pending_tasks
                                                       })