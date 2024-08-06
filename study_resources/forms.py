from django.forms import ModelForm
from .models import Bookmark, Video


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BookmarkForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class VideoForm(ModelForm):
    class Meta:
        models = Video
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
