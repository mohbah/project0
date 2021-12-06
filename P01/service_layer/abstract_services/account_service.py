from abc import ABC, abstractmethod


from entities import Account


class AccountService(ABC):
    def __init__(self, account_dao):
        self.account_dao: AccountDaoImpl = account_dao

    # create acount method
    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_get_account_information(self, account_id: int) -> Account:
        pass


    @abstractmethod
    def service_deposit_into_account_by_id(self, account_id: int, depositamount: int)->bool:
        pass

    @abstractmethod
    def service_withdraw_from_account_by_id(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def service_transfer_money_between_accounts_by_their_ids(self, id_to_withdrwa: int, id_to_deposit: int, amount:int) -> bool:
        pass


    @abstractmethod
    def service_delete_account_information(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def service_get_all_accounts_information(self) -> list[Account]:
        pass

    @abstractmethod
    def service_get_all_customer_accounts_by_id(self, coustomer_id: int) -> list[Account]:
        pass