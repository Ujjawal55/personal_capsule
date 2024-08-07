from django.forms import ModelForm
from .models import DailyTask


class DailyTaskForm(ModelForm):
    class Meta:
        model = DailyTask
        fields = ["title", "description"]

    def __init__(self, *args, **kwargs):
        super(DailyTaskForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
