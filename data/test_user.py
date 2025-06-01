import random
import string

def random_email():
    return f"autotest_{''.join(random.choices(string.ascii_lowercase, k=8))}@mail.com"

def random_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

USER = {"name": "Test User",
    "email": "svetlanabratchenko19123@yandex.ru",
    "password": "password123"
}
