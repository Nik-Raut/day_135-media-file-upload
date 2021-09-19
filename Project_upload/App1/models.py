from django.db import models

class Photos(models.Model):
    name=models.CharField(max_length=30)
    uploaded_photo=models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

