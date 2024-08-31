from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Notes
from notes.forms import NotesForm
from notes.utils import searchQuery, pagination


# TODO: have to add the functionality of the editing the message.
# TODO: have to add the else part for the not valid form of the error handling
# TODO: have to add the message functionality if the notes is created, deleted, edited
#


def notesListView(request):
    notes, search_query = searchQuery(request)
    notes, custom_range = pagination(request, notes, 3)
    context = {
        "notes": notes,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "notes/notes_list.html", context)


def notesDetailView(request, pk):
    note = get_object_or_404(Notes, id=pk, user=request.user)
    if not note.is_viewed:
        note.is_viewed = True
        note.save()
    context = {"note": note}
    return render(request, "notes/notes_detail.html", context)


def createNotesView(request):
    user = request.user
    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = user
            note.save()
            messages.success(request, "notes have been created successfully")
            return redirect("notes:notes-list")
        else:
            messages.error(request, "Error in the form")
    else:
        form = NotesForm()
    context = {"form": form}
    return render(request, "notes/create_notes.html", context)


def editNotesView(request, pk):
    note = get_object_or_404(Notes, id=pk, user=request.user)
    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            updated_note = form.save(commit=False)
            updated_note.user = request.user
            updated_note.save()
            messages.error(request, "Changes have been saved successfully")
            return redirect("notes:notes-detail", pk=updated_note.id)
        else:
            messages.error(request, "Error in the form")
    else:
        form = NotesForm(instance=note)
    context = {"form": form, "note": note}
    return render(request, "notes/edit_notes.html", context)


def deleteNotesView(request, pk):
    note = get_object_or_404(Notes, id=pk, user=request.user)
    if request.method == "POST":
        note.delete()
        messages.success(request, "your notes is deleted")
        return redirect("notes:notes-list")
    context = {"note": note}
    return render(request, "notes/delete_note.html", context)


def imageView(request, pk):
    note = get_object_or_404(Notes, id=pk, user=request.user)
    print("the image url is " + note.image.url)
    return render(request, "notes/view_image.html", {"note": note})
