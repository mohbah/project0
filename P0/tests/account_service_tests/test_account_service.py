from data_access_layer.Implimentation.account_postgres_dao import AccountPostgresDAO
from entities.Account import Account
from service_layer.implimentation_services.account_service_impl import AccountServiceImpl

account_dao = AccountPostgresDAO()
account_service = AccountServiceImpl(account_dao)
account = Account( 65, 1000, 28)


def test_validate_create_account_method():
        ACC = account_service.service_create_account(account)
        assert ACC.ballance == 1000

def test_validate__get_account_information():
        account1 = account_service.service_get_account_information(3)
        assert account1.ballance >0

def test_validate_deposit_into_account_by_id():
        x = account_service.service_deposit_into_account_by_id(3, 20)
        assert x == False

def test_validate__withdraw_from_account_by_id():

        x = account_service.service_withdraw_from_account_by_id(15,10)
        assert x == True

def test_validate_transfer_money_between_accounts_by_their_ids():
        x= account_service.service_get_account_information(21)
        y = x.ballance
        account_service.service_transfer_money_between_accounts_by_their_ids(21,22,10)
        x2= account_service.service_get_account_information(21)
        y2 = x2.ballance
        assert y == y2 + 10


def test_validate_delete_account_information():
        x = account_service.service_delete_account_information(50)
        assert x== False

def test_validate_get_all_accounts_information():
        x= account_service.service_get_all_accounts_information()
        assert len(x) > 4

def test_validate_get_all_customer_accounts_by_id():
        x= account_service.service_get_all_customer_accounts_by_id(28)
        assert len(x) >= 0



