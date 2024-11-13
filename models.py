from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # автоматически присваивает время создания
    def __str__(self):
        return self.name
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20)
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
