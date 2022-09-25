from django.db import models

# Create your models here.
class GeeksModels(models.Model):
    title = models.CharField(max_length = 200)
    desciption = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    # img = models.ImageField(upload_to = True)

    def _str_(self):
        return self.title