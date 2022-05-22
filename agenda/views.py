import calendar
from datetime import datetime, date, timedelta


from django.views import generic
from django.utils.safestring import mark_safe

from contracts.models import Contract
from .utils import Calendar

from django.contrib.auth.mixins import LoginRequiredMixin

class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Contract
    template_name = 'calendar.html'

    def get_queryset(self):
        return Contract.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the actual month to display the calendar
        d = get_date(self.request.GET.get('month', None))
        agenda = Calendar(d.year, d.month)
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


# def todo(request, event_id=None):
#     instance = Todo()
#     if event_id:
#         instance = get_object_or_404(Todo, pk=event_id)
#     else:
#         instance = Todo()
#
#     form = EventForm(request.POST or None, instance=instance)
#     if request.POST and form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('calendar'))
#     return render(request, 'event.html', {'form': form})

