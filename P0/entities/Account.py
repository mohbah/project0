class Account:

    def __init__(self, accountid: int, ballance: int, account_number: int, customer_id: int):
        self.accountid = accountid
        self.ballance = ballance
        self.account_number = account_number
        self.customer_id = customer_id

    def make_Account_dictionary(self):
        return {
            "accountId": self.accountid,
            "balance": self.ballance,
            "accountNumber": self.account_number,
            "customerId": self.customer_id,
        }

    def __str__(self):
        return "Account ID: {}, Balance: {}, Account#: {}, Customer ID: {}".format(self.accountid, self.ballance,self.account_number,self.customer_id)


    def __repr__(self):
        return "Account ID: {}, Balance: {}, Account#: {}, Customer ID: {}".format(self.account_number, self.ballance,self.account_number,self.customer_id)