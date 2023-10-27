from django.urls import path

from . import views

urlpatterns = [

    path('profs',views.ProfileListView.as_view(),name="profile.list"),
    path('profs/<int:pk>',views.ProfileDetailView.as_view(),name="profile.detail"),
    path('profs/<int:pk>/edit', views.ProfileUpdateView.as_view(), name="profile.update"),
    path('profs/<int:pk>/delete', views.ProfileDeleteView.as_view(), name="profile.delete"),
    path('profs/new',views.ProfileCreateView.as_view(),name="profile.new"),
    path("search/", views.SearchResultsView.as_view(), name="search_prof"),

    # path('profs/<data>', views.list, name="profile.list"),
]