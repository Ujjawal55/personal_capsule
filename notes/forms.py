from django.forms import ModelForm
from notes.models import Notes


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(NotesForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
