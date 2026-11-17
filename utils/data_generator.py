from faker import Faker
import random
import string

faker = Faker()


def generate_username():
    length = random.randint(8, 10)
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_password():
    length = random.randint(8, 10)
    characters = string.ascii_letters + string.digits + string.punctuation

    return "".join(random.choices(characters, k=length))
