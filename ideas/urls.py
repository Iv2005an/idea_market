from django.urls import path

from ideas import views


urlpatterns = [
    path("", views.ideas),
    path("my_ideas/", views.my_ideas, name="my_ideas"),
    path("create_idea/", views.create_idea, name="create_idea"),
    path("delete_idea/<int:pk>", views.delete_idea, name="delete_idea"),
    path("up_vote_idea/<int:pk>/", views.up_vote_idea, name="up_vote_idea"),
    path("down_vote_idea/<int:pk>/", views.down_vote_idea, name="down_vote_idea"),
]
