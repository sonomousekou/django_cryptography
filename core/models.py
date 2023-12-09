from cryptography.fernet import Fernet
from django.db import models

# Create your models here.
# Créez un objet Fernet avec la clé de chiffrement
encryption_key = '5F0-7PaK2xtDXDxsml1sT03Y8MY1nXIi-yDyGCFzxmE='
fernet = Fernet(encryption_key)

class Config(models.Model):
    cle = models.CharField(max_length=255, unique=True)
    valeur = models.BinaryField()

    def __str__(self):
        return self.cle

    def set_value(self, value):
        # Chiffrez la valeur avant de l'enregistrer dans la base de données
        self.valeur = fernet.encrypt(value.encode())

    def get_value(self):
        # Déchiffrez la valeur lors de la lecture de la base de données
        decrypted_value = fernet.decrypt(self.valeur)
        return decrypted_value.decode()

