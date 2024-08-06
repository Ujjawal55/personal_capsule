from django.forms import ModelForm
from .models import ResourcesList


class ResourcesListForm(ModelForm):
    class Meta:
        model = ResourcesList
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ResourcesListForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
