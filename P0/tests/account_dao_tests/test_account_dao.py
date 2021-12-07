
from data_access_layer.Implimentation.account_postgres_dao import AccountPostgresDAO
from entities.Account import Account

account_postgres_dao = AccountPostgresDAO()
accountt = Account(1, 110, 11)
depositedversionofpremadeaccount = Account(5, 187, 18)
withdrawlversionofpremadeaccount2 = Account(2, 10,  5)

ACC1 = Account(54, 10, 22)
ACC2 = Account(55, 20, 22)


def test_create_account_success():
    account: Account = account_postgres_dao.create_account(ACC2)
    assert account.accountid !=0


def test_get_account_by_id_success():
    returned_account: Account = account_postgres_dao.get_account_by_id(3)
    assert returned_account.accountid == 3


def test_deposit_into_account_by_id_success():
    result = account_postgres_dao.deposit_into_account_by_id(depositedversionofpremadeaccount)
    assert result.ballance == 187


def test_withdraw_from_account_by_id_success():
    result = account_postgres_dao.withdraw_from_account_by_id(withdrawlversionofpremadeaccount2)
    assert result.ballance == 10


def test_transfer_between_accounts_by_id_success():
    result = account_postgres_dao.transfer_money_between_accounts_by_their_ids(ACC1,ACC2)
    assert result


def test_delete_account_success():
    confirm_account_deleted = account_postgres_dao.delete_account_by_id(11)
    assert confirm_account_deleted


def test_get_all_accounts_success():
    account_list = account_postgres_dao.get_all_accounts()
    assert len(account_list) >1


def test_get_all_customer_accounts_by_id():
    customer_accounts_list = account_postgres_dao.get_all_customer_accounts_by_id(28)
    assert len(customer_accounts_list) !=0
