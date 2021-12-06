from custom_exceptions.CustomException import customexception
from data_access_layer.Implimentation.customer_dao_impl import CustomerDaoImpl
from data_access_layer.Implimentation.customer_postgres_dao import CustomerPostgresDAO
from entities import Customer
from service_layer.abstract_services.customer_service import CustomerService


class CustomerServiceImpl(CustomerService):
    def __init__(self, customer_postgres_dao):
        self.customer_postgres_dao: CustomerPostgresDAO = customer_postgres_dao

    def service_create_customer(self, customer: Customer) -> Customer:
        for customerss in self.customer_postgres_dao.get_all_customers():
            if customerss.ssn == customer.ssn:
                raise customexception("This SSN is already registered!")

        newcustomer = self.customer_postgres_dao.create_new_customer(customer)
        return newcustomer

    def service_get_all_customers(self) -> list[Customer]:
        return self.customer_postgres_dao.get_all_customers()

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        return self.customer_postgres_dao.get_customer_by_id(customer_id)


    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        x = len(self.customer_postgres_dao.get_all_customers())
        self.customer_postgres_dao.delete_customer_by_id(customer_id)
        if len(self.customer_postgres_dao.get_all_customers()) == x - 1:
            return True
        else:
            return False

    def service_update_customer(self, customer: Customer) -> Customer:
        for current_customer in self.customer_postgres_dao.get_all_customers():
            if current_customer.customerid == customer.customerid:
                if current_customer.first_name != customer.first_name:
                    raise customexception("Changing your first name is not allowed!!")
                if current_customer.last_name != customer.last_name:
                    raise customexception("Changing your last name is not allowed!!")
                if current_customer.ssn != customer.ssn:
                    raise customexception("Changing your ssn is not allowed!!")

        return self.customer_postgres_dao.update_customer(customer)
