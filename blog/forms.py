from django import forms
from .models import ScheduleFile

class ScheduleFileForm(forms.ModelForm):
    class Meta:
        model = ScheduleFile
        fields = "__all__"
