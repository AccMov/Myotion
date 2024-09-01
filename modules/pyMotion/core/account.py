class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.email = None
        self.phone = None
        self.address = None
        self.city = None
        self.state = None
        self.zipcode = None
        self.country = None
        self.birthday = None
        self.apikey = username + "-apikey"

    def __str__(self):
        return (
            "Username: %s\nEmail: %s\nPhone: %s\nAddress: %s\nCity: %s\nState: %s\nZipcode: %s\nCountry: %s\nBirthday: %s"
            % (
                self._username,
                self._email,
                self._phone,
                self._address,
                self._city,
                self._state,
                self._zipcode,
                self._country,
                self._birthday,
            )
        )

    def key_from_json(self, json):
        self.tenantId = json["tenantId"]
        self.externalKey = json["externalKey"]
        self.apikey = json["apiKey"]
