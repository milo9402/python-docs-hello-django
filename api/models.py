from django.db import models
from django.contrib.auth.models import AbstractUser

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.username), filename])

class User(AbstractUser):

    email = models.EmailField(verbose_name="User Email", unique=True, max_length=100)

    second_name = models.CharField(max_length=100, null=True, blank=True)
    second_lastname = models.CharField(max_length=100, null=True, blank=True)

    # Tipos de documentos de identidad

    CEDULA_CIUDADANIA = 'CC'
    TARJETA_IDENTIDAD = 'TI'
    CEDULA_EXTRANGERIA = 'CE'
    NIT = 'NIT'
    DOCUMENT_TYPE_CHOICES = (
        (CEDULA_CIUDADANIA, 'Cedula ciudadania'),
        (TARJETA_IDENTIDAD, 'Tarjeta de identidad'),
        (CEDULA_EXTRANGERIA, 'Cedula extranjeria'),
        (NIT, 'Nit'),
    )
    document_type = models.CharField(
        max_length=3,
        choices=DOCUMENT_TYPE_CHOICES,
        default=CEDULA_CIUDADANIA,
    )

    document = models.IntegerField(null=True, blank=False)

    picture = models.ImageField(upload_to=nameFile, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # Por defecto seran requeridos el email y password

    create=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.username)
