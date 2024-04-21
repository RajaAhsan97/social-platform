from django.db import models

# Create your models here.

class groupAdmin(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.username

class Group(models.Model):
    admin = models.ForeignKey(groupAdmin, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)    
    created = models.DateTimeField(auto_now_add=True)
    # members = models.PositiveIntegerField(unique=True, null=True)

    def __str__(self):
        return self.name
    
class GroupJoinedMembers(models.Model):
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE)
    member = models.ForeignKey(groupAdmin, on_delete=models.CASCADE)

    def __str__(self):
        # print("Group Members: ", str(self.group_name))
        return str(self.group_name)

class Post(models.Model):
    group = models.ForeignKey(Group, related_name="posts", on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"{self.group} {self.message}"