from django.urls import include, path

from accounts import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
