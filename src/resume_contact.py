class Contact:
    def __init__(self, email : str, phone = '', location = ''):
        self.email = email
        self.phone = phone
        self.location = location
        
    def set_email(self, email : str) -> None:
        self.email = email
        
    def set_phone(self, phone : str) -> None:
        self.phone = phone
        
    def set_location(self, location : str) -> None:
        self.location = location