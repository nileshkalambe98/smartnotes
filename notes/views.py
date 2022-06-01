from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from .models import Notes
from django.views.generic import DetailView, ListView , CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .forms import NotesForm

class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDeleteView(DeleteView):
        model = Notes
        success_url = '/smart/notes'
        template_name = 'notes/notes_delete.html'

## def list(request):
##    all_notes = Notes.objects.all()
##    return render(request, 'notes/notes_list.html',{'notes': all_notes})

class NotesUpdateView(UpdateView):
        model = Notes
        success_url = '/smart/notes'
        form_class = NotesForm


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


 ## def detail(request,pk):
##    try:
##        note = Notes.objects.get(pk=pk)
##    except Notes.DoesNotExist  :
##        raise Http404("Note does not exist")

##    return render(request, 'notes/notes_detail.html' ,{'note' :note })
