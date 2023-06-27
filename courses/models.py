from django.db import models
from django.contrib.auth.models import User

def sample():
    return {}

class Problem(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    sampletests = models.JSONField(default=sample)
    tests = models.JSONField(default=sample)
    solvers = models.ManyToManyField(User, related_name="problem_solvers")
    errors = models.ManyToManyField(User, related_name="problem_errors")

class Attempt(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField(default="", null=True, blank=True)
    status = models.CharField(max_length=20, default="Running", null=True, blank=True)
    language = models.CharField(max_length=20)
    time = models.FloatField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Lesson(models.Model):
    title = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000, null=True, blank=True)
    content = models.TextField()
    showers = models.ManyToManyField(User, related_name="lesson_showers")
    enders = models.ManyToManyField(User, related_name="lesson_enders")
    problems = models.ManyToManyField(Problem, related_name="lesson_problems")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:20] + "..."
    
    def save(self, *args, **kwargs):
        self.url = self.title.lower()
        self.url = self.url.replace(" ", "_")
        self.url = self.url.replace(".", "")
        self.url = self.url.replace(",", "")
        return super().save(*args, **kwargs)
    
    def short_title(self):
        return self.title[:20] + "..."
    
    def count_showers(self):
        return self.showers.count()

    def count_enders(self):
        return self.enders.count()
    
