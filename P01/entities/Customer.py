class Customer:

    def __init__(self, customerid: int, ssn: int, first_name: str, last_name: str, phonenumber: int):
        self.customerid = customerid
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.phonenumber = phonenumber

    def make_customer_dictionary(self):
        return {
            "customerid": self.customerid,
            "ssn": self.ssn,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "phoneNumber": self.phonenumber,

        }

    def __repr__(self):
        return "Customer ID: {}, SSN: {}, FirstName: {}, LastName: {}, PhoneNumber: {}".format(self.customerid, self.ssn,
                                                                                   self.first_name,
                                                                                   self.last_name,
                                                                                               self.phonenumber)
