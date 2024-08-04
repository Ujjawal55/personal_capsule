from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Notes
from notes.forms import NotesForm
from notes.utils import searchQuery
# Create your views here.

# TODO: have to add the functionality of the editing the message.
# TODO: have to add the else part for the not valid form of the error handling


def notesListView(request):
    notes, search_query = searchQuery(request)
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
    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("notes-list")
    else:
        form = NotesForm()
        context = {"form": form}

        return render(request, "notes/create_notes.html", context)


def editNotesView(request, pk):
    note = get_object_or_404(Notes, id=pk)
    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            updated_note = form.save(commit=False)
            updated_note.save()
            return redirect("notes-detail", pk=updated_note.id)
    else:
        form = NotesForm(instance=note)
    context = {"form": form}
    return render(request, "notes/edit_notes.html", context)
