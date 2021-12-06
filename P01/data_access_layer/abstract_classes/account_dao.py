from abc import ABC, abstractmethod

from entities.Account import Account


class AccountDao(ABC):

    @abstractmethod
    def create_account(self, account : Account)-> Account:
        pass

    @abstractmethod
    def get_account_by_id(self,account_id: int)-> Account:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, account : Account)->bool:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, account: Account) -> Account:
        pass

    @abstractmethod
    def transfer_money_between_accounts_by_their_ids(self,account_to_withdrwa: Account, account_to_deposit: Account)-> bool:
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id: int)-> bool:
        pass



    @abstractmethod
    def get_all_accounts(self)-> list[Account]:
        pass

    @abstractmethod
    def get_all_customer_accounts_by_id(self, coustomer_id: int) -> list[Account]:
        pass