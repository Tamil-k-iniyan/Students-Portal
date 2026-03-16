from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    team_code = models.CharField(max_length=10, unique=True)
    max_members = models.IntegerField()

    def __str__(self):
        return self.team_name


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name