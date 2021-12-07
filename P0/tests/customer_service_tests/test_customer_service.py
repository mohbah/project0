
from custom_exceptions.CustomException import customexception
from data_access_layer.Implimentation.customer_postgres_dao import CustomerPostgresDAO
from entities.Customer import Customer
from service_layer.implimentation_services.customer_service_impl import CustomerServiceImpl

customer_dao = CustomerPostgresDAO()
customer_service = CustomerServiceImpl(customer_dao)

customer_on_database= Customer(10,999," mohsen", "tj",1)
customer_not_on_database= Customer(81, 98,"Beck", "Ron", 9137378739)

def test_validate_create_customer_method():
     customer_service.service_create_customer(customer_not_on_database)
     assert len(customer_service.service_get_all_customers())> 0

def test_validate_get_all_customers_information():
    x = customer_service.service_get_all_customers()
    assert len(x) > 3

def test_validate__get_customer_information():
    customer = customer_service.service_get_customer_by_id(35)
    assert customer.last_name == "tj"

def test_validate_delete_account_information():
    x = customer_service.service_delete_customer_by_id(27)
    assert x == False

def test_validate_update_customer():
    x = customer_service.service_update_customer(customer_on_database)
    assert x.phonenumber ==1


