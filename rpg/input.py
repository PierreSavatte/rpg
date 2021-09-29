def validate(value: str) -> str:
    return value.lower().replace(" ", "_")


def ask(message=None, do_validate=True) -> str:
    if message:
        print(message)
    value = input("> ")
    if do_validate:
        return validate(value)
    else:
        return value


def is_affirmative(value):
    return value in ["yes", "y", "true"]
