from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models import Q

from .models import User, Profile, Scrawl, Comment
from .forms import ScrawlForm


@login_required
def home(request):
    followed_scrawls = Scrawl.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by(
        "-created_at")

    if request.method == "POST":
        if request.POST.__contains__("quill"):
            scrawl_id = request.POST.get("quill")
            scrawl = get_object_or_404(Scrawl, pk=scrawl_id)
            if scrawl in request.user.quilled_scrawls.all():
                scrawl.quilled_by.remove(request.user)
                scrawl.quills -= 1
            else:
                scrawl.quilled_by.add(request.user)
                scrawl.quills += 1
            scrawl.save()
            return redirect("scrawl:home")

        if request.POST.__contains__("save"):
            scrawl_id = request.POST.get("save")
            scrawl = get_object_or_404(Scrawl, pk=scrawl_id)
            if scrawl in request.user.saved_scrawls.all():
                scrawl.saved_by.remove(request.user)
            else:
                scrawl.saved_by.add(request.user)
            scrawl.save()
            return redirect("scrawl:home")

    return render(request, "scrawl/home.html", {"scrawls": followed_scrawls})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    total_quills = Scrawl.objects.filter(user__profile=profile).aggregate(Sum("quills", default=0))
    total_following = profile.follows.all().count()
    total_followers = profile.followed_by.all().count()
    following = User.objects.filter(profile__in=profile.follows.all()).order_by("username")
    followers = User.objects.filter(profile__in=profile.followed_by.all()).order_by("username")

    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "scrawl/profile.html", {"profile": profile, "total_quills": total_quills,
                                                   "total_followers": total_followers, "total_following": total_following, "following": following,
                                                   "followers": followers})


def following(request, pk):
    profile = Profile.objects.get(pk=pk)
    following = User.objects.filter(profile__in=profile.follows.all()).order_by("username")
    followers = User.objects.filter(profile__in=profile.followed_by.all()).order_by("username")

    return render(request, "scrawl/following.html", {"profile": profile, "following": following,
                                                     "followers": followers})


def create_scrawl(request):
    form = ScrawlForm(request.POST or None)

    if request.method == "POST":
        form = ScrawlForm(request.POST)
        if form.is_valid():
            scrawl = form.save(commit=False)
            scrawl.user = request.user
            scrawl.save()
            return redirect("scrawl:home")

    return render(request, "scrawl/create_scrawl.html", {"form": form})


def comments(request, pk):
    scrawl = get_object_or_404(Scrawl, pk=pk)
    all_comments = scrawl.comments.all().order_by("-quills")

    if request.method == "POST":
        if request.POST.__contains__("comment"):
            comment = Comment()
            comment.user = request.user
            comment.scrawl = scrawl
            comment.body = request.POST.get("body")
            comment.save()
            return redirect("scrawl:comments", pk=pk)

        if request.POST.__contains__("quill"):
            comment = get_object_or_404(Comment, pk=request.POST.get("quill"))
            if comment in request.user.quilled_comments.all():
                comment.quilled_by.remove(request.user)
                comment.quills -= 1
            else:
                comment.quilled_by.add(request.user)
                comment.quills += 1
            comment.save()
            return redirect("scrawl:comments", pk=pk)

    return render(request, "scrawl/comments.html", {"comments": all_comments})


def quillboard(request):
    top_scrawls = Scrawl.objects.all().order_by('-quills')[:20]  # top 20 to be selected

    return render(request, "scrawl/quillboard.html", {"top_scrawls": top_scrawls})
