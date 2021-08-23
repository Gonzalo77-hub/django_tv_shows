from django.db import models

class ShowManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}
        print(postData['title'])
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['title']) < 2:
            errors["title"] = "El largo del titulo debe ser mayor a 2 caracteres"
        if len(postData['Network']) < 3:
            errors["Network"] = "El largo del network debe ser mayor a 3 caracteres"
        if 1 <= len(postData['desc']) < 10 :
            errors["desc"] = "El largo de la descripcion debe ser mayor a 10 caracteres"
        if Show.objects.filter(title=postData['title']).exists():
            errors['existe'] ='El titulo ya existe, favor ingresar otro'
        print(errors)
        return errors
    def edit_validator(self, postData):
        errors = {}
        print(postData['edit_title'])
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['edit_title']) < 2:
            errors["ed_title"] = "El largo del titulo debe ser mayor a 2 caracteres"
        if len(postData['edit_Network']) < 3:
            errors["ed_Network"] = "El largo del network debe ser mayor a 3 caracteres"
        if len(postData['edit_desc']) < 10:
            errors["ed_desc"] = "El largo de la descripcion debe ser mayor a 10 caracteres"
        if Show.objects.filter(title=postData['edit_title']).exclude(title=postData['edit_title']).exists():
            errors['existe'] ='El titulo ya existe, favor ingresar otro'
        print(errors)
        print(errors)
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=25)
    desc = models.CharField(max_length=255)
    Release = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()  

    def __repr__(self):
        return f"Nombre Serie: {self.title}, plataforma: {self.network}"