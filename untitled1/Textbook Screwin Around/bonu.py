#FIRAS ABOUSHAMALAH
#VAISHVIK PATEL
#KROHMAN GAVIN

class profile:
    def __init__(self, name, age, city, id):
        self._name = name
        self._age = age
        self._city = city
        self._id = id
        self._status = ""
        self._profile = ""
        self._friendsList = []

    def relationshipStatus(self, status):
        self._status = status

    def getStatus(self):
        return self._status

    def profileStatus(self, profile):
        self._profile = profile

    def getProfile(self):
        return self._profile

    def _init_addFriend(self):
        self._friendsList.append(profile)



