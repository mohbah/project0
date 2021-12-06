
from custom_exceptions.CustomException import customexception

from data_access_layer.Implimentation.account_postgres_dao import AccountPostgresDAO
from entities import Account
from service_layer.abstract_services.account_service import AccountService
from psycopg import connect, OperationalError, Error


class AccountServiceImpl(AccountService):

    def __init__(self, account__postgres_dao):
        self.account_postgres_dao: AccountPostgresDAO = account__postgres_dao

    def service_create_account(self, account: Account) -> Account:
        try:
            return self.account_postgres_dao.create_account(account)
        except (Exception, Error) as error:
            return ("Error while connecting to PostgreSQL", error)

    def service_get_account_information(self, account_id: int) -> Account:
        return self.account_postgres_dao.get_account_by_id(account_id)

    def service_deposit_into_account_by_id(self, accountidd: int, depositamount: int) -> bool:

        for account_in_list in self.account_postgres_dao.get_all_accounts():
            if account_in_list.accountid == accountidd:
                account_in_list.ballance += depositamount
                self.account_postgres_dao.deposit_into_account_by_id(account_in_list)
        return False

    def service_withdraw_from_account_by_id(self, accountidd: int, withdrawamount: int):
        for account_in_list in self.account_postgres_dao.get_all_accounts():
            if account_in_list.accountid == accountidd:
                if withdrawamount >= 0 and account_in_list.ballance >= withdrawamount:
                    account_in_list.ballance -= withdrawamount
                    self.account_postgres_dao.withdraw_from_account_by_id(account_in_list)
                    return True
                else:
                    return False









    def service_transfer_money_between_accounts_by_their_ids(self, id_to_withdrwa: int, id_to_deposit: int,amount: int) -> bool:
        for account_in_list in self.account_postgres_dao.get_all_accounts():
            for account_in_list1 in self.account_postgres_dao.get_all_accounts():
                if account_in_list.accountid==id_to_withdrwa:
                    if account_in_list1.accountid== id_to_deposit:
                        if amount >= 0 and account_in_list.ballance >= amount:
                            account_in_list.ballance -= amount
                            self.account_postgres_dao.withdraw_from_account_by_id(account_in_list)
                            account_in_list1.ballance += amount
                            self.account_postgres_dao.deposit_into_account_by_id(account_in_list1)
                            return True

                        else:
                            return False




    def service_delete_account_information(self, account_id: int):
        x = len(self.account_postgres_dao.get_all_accounts())
        self.account_postgres_dao.delete_account_by_id(account_id)
        if len(self.account_postgres_dao.get_all_accounts()) == x - 1:
            return True
        else:
            return False

    def service_get_all_accounts_information(self) -> list[Account]:
        return self.account_postgres_dao.get_all_accounts()

    def service_get_all_customer_accounts_by_id(self, coustomer_id: int) -> list[Account]:
        return self.account_postgres_dao.get_all_customer_accounts_by_id(coustomer_id)
