from datetime import timedelta

from django.db.models import Q
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Profile
from django.views.generic import DetailView,ListView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from . forms import ProfileForm

# def datefunc(request,data):
#     dafter = (data + timedelta(days=30)).isoformat()
#     return render(request,'pawn/profdetails.html',{'dafter':dafter})

class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = "pawn/deleteprofile.html"
    success_url = '/mbp/profs/'
    form_class = ProfileForm
    login_url = '/admin'

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model =Profile
    template_name = "pawn/newprofileform.html"
    success_url = '/mbp/profs/'
    form_class = ProfileForm
    login_url = '/admin'

class ProfileCreateView(LoginRequiredMixin,CreateView):
    model = Profile
    template_name = "pawn/newprofileform.html"
    success_url = '/mbp/profs'
    form_class = ProfileForm
    login_url = '/admin'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ProfileListView(LoginRequiredMixin,ListView):
    model= Profile
    context_object_name = "pawn"
    template_name = "pawn/listdisplay.html"
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.pawn.all()

# def list(request):
#         all_notes = Profile.objects.filter(amount__gte=200000).values()
#         return render(request,'pawn/listdisplay.html',{'pawn': all_notes})

class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = Profile
    context_object_name = "pawn"
    template_name = "pawn/profdetails.html"
    login_url = '/admin'

class SearchResultsView(ListView):
    model = Profile
    template_name = "pawn/search_prof.html"
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Profile.objects.filter(
            Q(first_name__icontains=query)
        )
        return object_list