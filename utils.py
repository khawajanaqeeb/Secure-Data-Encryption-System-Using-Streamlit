import base64
import hashlib

def generate_key_from_password(password):
    """
    Converts a password into a valid Fernet key (base64-encoded 32-byte key)
    """
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)
