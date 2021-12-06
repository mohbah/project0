from data_access_layer.abstract_classes.customer_dao import CustomerDAO
from entities.Customer import Customer


class CustomerDaoImpl(CustomerDAO):

    customer1 = Customer(1, 121 , "moh", "bah", 121221)
    cus = Customer(2, 144421, "mok", "bok", 1212112121234)
    c1 = Customer(3, 62853, " ali", "ramini", 9137378739)

    customer_list = [cus, c1, customer1]

    cutomer_id_generator = 100

    def create_new_customer(self, customer: Customer) -> Customer:
        newcustomer = customer
        CustomerDaoImpl.cutomer_id_generator += 1
        newcustomer.customerid = CustomerDaoImpl.cutomer_id_generator
        CustomerDaoImpl.customer_list.append(newcustomer)
        return newcustomer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        for customer in CustomerDaoImpl.customer_list:
            if customer.customerid == customer_id:
                return customer

    def update_customer(self, customer: Customer) -> Customer:
        for customer_in_list in CustomerDaoImpl.customer_list:
            if customer_in_list.customerid == customer.customerid:
                index = CustomerDaoImpl.customer_list.index(customer_in_list)
                CustomerDaoImpl.customer_list[index] = customer
                return customer

    def delete_customer_by_id(self, customer_id: int) -> bool:

        for customer_in_list in CustomerDaoImpl.customer_list:
            if customer_in_list.customerid == customer_id:
                index = CustomerDaoImpl.customer_list.index(customer_in_list)
                del CustomerDaoImpl.customer_list[index]
        return True


    def get_all_customers(self) -> list[Customer]:
        return CustomerDaoImpl.customer_list
