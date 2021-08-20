from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=25)
    desc = models.CharField(max_length=255)
    Release = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __repr__(self):
        return f"Nombre Serie: {self.title}, plataforma: {self.network}"