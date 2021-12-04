from data_access_layer.Implimentation.customer_dao_impl import CustomerDaoImpl
from data_access_layer.Implimentation.customer_postgres_dao import CustomerPostgresDAO
from entities.Customer import Customer

customer_postgres_dao = CustomerPostgresDAO()

testcustomer = Customer(0, 999, " Joe", "tj", 87787)
updatedone = Customer(11, 999 , "mo111hsen", "tj", 10000122)

def test_create_customer_success():
    created_customer = customer_postgres_dao.create_new_customer(testcustomer)
    assert created_customer.customerid !=0

def test_get_customer_by_id_success():
    returned_customer =  customer_postgres_dao.get_customer_by_id(10)
    assert returned_customer.customerid == 10

def test_update_customer():
    result = customer_postgres_dao.update_customer(updatedone)
    assert result.phonenumber == 10000122

def test_select_all_customers_success():
        customers = customer_postgres_dao.get_all_customers()
        print(customers)
        assert len(customers) >= 2

def test_delete_customer_by_id():
    confirm_deleted = customer_postgres_dao.delete_customer_by_id(11)
    assert confirm_deleted