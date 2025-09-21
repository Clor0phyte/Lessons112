def validate_password(password):
    return len(password) > 8 and any(ch.isdigit() for ch in password)

print(validate_password("mypassword123"))