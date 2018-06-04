class User(object):
    """ Docstring for User """
    def __init__(self, user_id, first_name, last_name, 
                 status, login, email, password,
                 user_type, unity):
        super(User, self).__init__()

        self._user_id = int(user_id)
        self._first_name = first_name
        self._last_name = last_name
        self._status = status
        self._login = login
        self._email = email
        self._password = password
        self._type = user_type
        self._unity = unity

    @property
    def user_id(self):
        return self._user_id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def status(self):
        return self._status

    @property
    def login(self):
        return self._login

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def user_type(self):
        return self._type

    @property
    def unity(self):
        return self._unity

        