from django.shortcuts import render
from notes.models import Notes
from notes.forms import NotesForm
# Create your views here.
# TODO: have to add the functionality of the editing the message.


def notesListView(request):
    notes = Notes.objects.all()

    context = {"notes": notes}
    return render(request, "notes/notes_list.html", context)


def notesDetailView(request, pk):
    note = Notes.objects.get(id=pk)
    if not note.is_viewed:
        note.is_viewed = True
        note.save()
    context = {"note": note}
    return render(request, "notes/notes_detail.html", context)


def createNotesView(request):
    form = NotesForm()

    context = {"form": form}

    return render(request, "notes/create_notes.html", context)
