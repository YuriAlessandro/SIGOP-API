class Avaliation(object):

    def __init__(self, avaliation_id, date, offer_id,
                user_id, value, text):
        super(Avaliation, self).__init__()
        self._avaliation_id = avaliation_id
        self._date = date
        self._offer_id = offer_id
        self._user_id = user_id
        self._value = value
        self._text = text

    @property
    def avaliation_id(self):
        return self._avaliation_id

    @property
    def date(self):
        return self._date

    @property
    def offer_id(self):
        return self._offer_id

    @property 
    def user_id(self):
        return self._user_id

    @property
    def value(self):
        return self._value
    
    @property
    def text(self):
        return self._text
