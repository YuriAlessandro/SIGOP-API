class Favorite(object):
    """docstring for Favorite"""
    def __init__(self, user_id, offer_id):
        super(Favorite, self).__init__()
        self._offer_id = offer_id
        self._user_id = user_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def offer_id(self):
        return self._offer_id

