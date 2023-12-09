from cryptography.fernet import Fernet

# Générez une clé de chiffrement (vous pouvez la stocker en toute sécurité ailleurs)
encryption_key = Fernet.generate_key()

print(encryption_key)