from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from ideas.forms import CreateIdeaForm
from ideas.models import Idea


def ideas(request):
    ideas = Idea.objects.all().order_by("-votes")
    return render(request, "ideas/ideas.html", {"ideas": ideas})


@login_required
def my_ideas(request):
    ideas = Idea.objects.filter(user=request.user).order_by("-votes")
    return render(request, "ideas/my_ideas.html", {"ideas": ideas})


@login_required
def create_idea(request):
    if request.method == "GET":
        form = CreateIdeaForm()
    elif request.method == "POST":
        form = CreateIdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user
            idea.save()
            return redirect("my_ideas")
    return render(request, "ideas/create_idea.html", {"form": form})


@login_required
def delete_idea(request, pk):
    ref_url = request.META["HTTP_REFERER"]
    if ref_url.split("/")[-2] == "my_ideas":
        ideas = Idea.objects.filter(user=request.user).order_by("-votes")
    else:
        ideas = Idea.objects.all().order_by("-votes")
    idea_to_delete = ideas.get(pk=pk)
    index = list(ideas).index(idea_to_delete) - 1
    idea_to_delete.delete()
    idea_id = ""
    if index >= 0:
        idea_id = f"#idea_{ideas[index].pk}"
    return redirect(f"{ref_url}{idea_id}")


@login_required
def up_vote_idea(request, pk):
    ideas = Idea.objects.all().order_by("-votes")
    idea_to_vote = ideas.get(pk=pk)
    idea_to_vote.votes += 1
    idea_to_vote.save()
    return redirect(f"../../#idea_{pk}")


@login_required
def down_vote_idea(request, pk):
    ideas = Idea.objects.all().order_by("-votes")
    idea_to_vote = ideas.get(pk=pk)
    idea_to_vote.votes -= 1
    idea_to_vote.save()
    return redirect(f"../../#idea_{pk}")
