from django.forms import ModelForm, DateInput, CheckboxInput
from .models import Task
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class CheckboxInput(forms.CheckboxInput):
    input_type = 'checkbox'


class TaskForm(ModelForm):
  class Meta:
    model = Task
    completed = forms.CheckboxInput()
    widgets = {
      'start_time': DateInput(),
      'end_time': DateInput(),
      # 'completed': CheckboxInput(attrs={'class': 'checkbox'}),
    }
    fields = ['title', 'description', 'start_time', 'end_time', 'completed']

    def __init__(self, *args, **kwargs):
      super(TaskForm, self).__init__(*args, **kwargs)
      self.fields['start_time'].input_formats = ('%Y-%m-%d',)
      self.fields['end_time'].input_formats = ('%Y-%m-%d',)