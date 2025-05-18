import re

def name():
    # Pattern for valid names (e.g., "John Cena")
    return re.compile(r'^[A-Z][a-z]+(?: [A-Z][a-z]+)*$')

def phone_number():
    # Pattern for US phone numbers in various formats
    return re.compile(r'^\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}$')

def email_address():
    # Pattern for valid email addresses
    return re.compile(r'^[\w.-]+@[\w-]+(?:\.[\w-]+)+$')
