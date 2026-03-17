from django.shortcuts import render

# Create your views here.
from .models import ProjectFile, Team

def upload_file(request):
    if request.method == "POST":
        team_id = request.POST.get("team_id")
        file = request.FILES.get("file")

        team = Team.objects.get(id=team_id)

        ProjectFile.objects.create(team=team, file=file)

        return render(request, "upload.html", {"message": "File uploaded"})

    return render(request, "upload.html")

def give_feedback(request):
    message = ""

    if request.method == "POST":
        team_id = request.POST.get("team_id")
        comment = request.POST.get("comment")

        team = Team.objects.get(id=team_id)

        Feedback.objects.create(team=team, comment=comment)

        message = "Feedback submitted"

    return render(request, "feedback.html", {"message": message})