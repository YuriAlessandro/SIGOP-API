class Offer(object):
    """docstring for Offer"""
    def __init__(self, offer_id, title, description, user_id, end_offer, email, phone):
        super(Offer, self).__init__()
        self._offer_id = offer_id
        self._title = title
        self._description = description
        self._end_offer = end_offer
        self._user_id = user_id
        self._email = email
        self._phone = phone
        self._type = offer_type
        self._salary_aids = salary_aids
        self._salary_total = salary_total
        self._location = location
        self._latitude = latitude
        self._longitude = longitude

    @property
    def offer_id(self):
        return self._offer_id
    
    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def end_offer(self):
        return self._end_offer

    @property
    def user_id(self):
        return self._user_id
    
    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone
    
    @property
    def offer_type(self):
        return self._offer_type
    
    @property
    def salary_aids(self):
        return self._salary_aids

    @property
    def salary_total(self):
        return self._salary_total

    @property
    def location(self):
        return self._location
    
    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude   