from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = [".com", ".bg", ".org", ".net"]

pattern_name = r"[\w+\.]+"
pattern_domain = r"\.[a-z]+"

email = input()

while email != "End":

    try:
        if len(email.split("@")[0]) < 5:
            raise NameTooShortError("Name must be more than 4 characters")

        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")

        if findall(pattern_domain, email)[-1] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    except IndexError:
        print("Invalid email")

    else:
        print("Email is valid")

    email = input()
