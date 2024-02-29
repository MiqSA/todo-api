class ErrorInCreateUser(Exception):
    pass


class UserAlreadyExistError(Exception):
    pass


class UniqueValueError(Exception):
    pass


class EmailIncorrectError(Exception):
    pass


class PasswordIncorrectError(Exception):
    pass


class LimitNotSupportedError(Exception):
    pass


class FieldNotSupportedError(Exception):
    pass


class DataNotFound(Exception):
    pass