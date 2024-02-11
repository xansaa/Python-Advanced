import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


class PasswordTooShortError(Exception):
    pass


class PasswordDigitError(Exception):
    pass


class PasswordLowerAndUpperLetter(Exception):
    pass


class PasswordLetterAndDigit(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_NAME_SYMBOLS_COUNT = 4

pattern_name = r'\w+'


def validate_email(emails):
    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email should contain only one @ symbol!")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")
    if len(email.split("@")[0]) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameTooShortError("Name must be more than 4 characters!")
    if email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")
    if re.findall(pattern_name, email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores!")

    print("Email is valid")
    return True


def validate_password(passwords):
    if not password.isalnum():
        raise PasswordLetterAndDigit("Password must contain only letters and digits!")
    if not (any(char.islower() for char in password) and any(char.isupper() for char in password)):
        raise PasswordLowerAndUpperLetter("Password must contain at least one lowercase and one uppercase letter!")
    if not any(char.isdigit() for char in password):
        raise PasswordDigitError("Password must contain at last one digit!")
    if not (8 <= len(password) <= 14):
        raise PasswordTooShortError("Password length should be between 8 and 14 characters and digits!")


email = input("Enter email: ")

while email != "End":
    try:
        if validate_email(email):
            password = input("Enter password: ")

            while password != "End":
                try:
                    validate_password(password)
                    print("Valid password")
                    break
                except (PasswordLetterAndDigit, PasswordLowerAndUpperLetter, PasswordDigitError, PasswordTooShortError) as e:
                    print(f"Validation Error: {e}")

                password = input("Enter the next password: ")

    except (MoreThanOneAtSymbol, MustContainAtSymbolError, InvalidDomainError, InvalidNameError, NameTooShortError) as e:
        print(f"Validation Error: {e}")

    email = input("Enter the next email: ")
