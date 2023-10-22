from django.db import models

# class Authors(models.Model):
#     fullname = models.CharField(max_length=120)
#     born_date = models.DateField(auto_now_add=True)
#     born_location = models.CharField(max_length=120)
#     description = models.CharField(max_length=120)


# class Tag(models.Model):
#     name = models.CharField(max_length=25, null=False, unique=True)


# class Quotes(models.Model):
#     tags = models.ManyToManyField(Tag)
#     author = models.ManyToManyField(Authors)
#     quote =  models.TextField(max_length=1250)





# class Tag(models.Model):
#     name = models.CharField(max_length=25, null=False, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=["user", "name"], name="tag of username")
#         ]

#     def __str__(self) -> str:
#         return f"{self.name}"


# class Note(models.Model):
#     name = models.CharField(max_length=50, null=False)
#     description = models.CharField(max_length=150, null=False)
#     done = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     tags = models.ManyToManyField(Tag)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

#     def __str__(self) -> str:
#         return f"{self.name}"