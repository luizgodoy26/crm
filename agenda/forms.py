from django.forms import ModelForm, DateInput
from .models import Event
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(),
      'end_time': DateInput(),
    }
    fields = '__all__'

    def __init__(self, *args, **kwargs):
      super(EventForm, self).__init__(*args, **kwargs)
      # input_formats to parse HTML5 datetime-local input to datetime field
      self.fields['start_time'].input_formats = ('%Y-%m-%d',)
      self.fields['end_time'].input_formats = ('%Y-%m-%d',)