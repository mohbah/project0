from data_access_layer.abstract_classes.account_dao import AccountDao
from entities.Account import Account
from entities.Customer import Customer
from Util.database_connection import connection
from psycopg import connect, OperationalError, Error


class AccountPostgresDAO(AccountDao):


    def create_account(self, account: Account) -> Account:

        sql = "insert into account values(default, %s, %s) returning account_id"

        cursor = connection.cursor()

        cursor.execute(sql, (account.ballance, account.customer_id))

        connection.commit()
        acco = cursor.fetchone()[0]
        account.accountid = acco

        return account



    def get_account_by_id(self, account_id: int) -> Account:
        try:
            sql = "select * from account where account_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [account_id])
            account_record = cursor.fetchone()
            account = Account(*account_record)
            return account
        except TypeError as e:
            return str(e)

    def deposit_into_account_by_id(self, account: Account) -> bool:
        sql = "update account set balance= %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account.ballance, account.accountid))
        connection.commit()
        return account

    def withdraw_from_account_by_id(self, account: Account) -> Account:
        sql = "update account set balance= %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account.ballance, account.accountid))
        connection.commit()
        return account

    def transfer_money_between_accounts_by_their_ids(self, account_to_withdrwa: Account,
                                                     account_to_deposit: Account) -> bool:
        sql = "update account set balance= %s where account_id = %s"
        sql1 = "update account set balance= %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account_to_withdrwa.ballance, account_to_withdrwa.accountid))
        cursor.execute( sql1,(account_to_deposit.ballance, account_to_deposit.accountid))
        connection.commit()
        return True

    def delete_account_by_id(self, account_id: int) -> bool:
        sql = "delete from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True

    def get_all_accounts(self) -> list[Account]:
        sql = " select * from account"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_list = cursor.fetchall()
        list = []
        for account in account_list:
            list.append(Account(*account))
        return list

    def get_all_customer_accounts_by_id(self, coustomer_id: int) -> list[Account]:
        sql = "select * from account where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [coustomer_id])
        account_records = cursor.fetchall()
        account_list = []
        for account in account_records:
            account_list.append(Account(*account))
        return account_list
