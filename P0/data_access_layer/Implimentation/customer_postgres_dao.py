from data_access_layer.abstract_classes.customer_dao import CustomerDAO
from entities.Customer import Customer
from Util.database_connection import connection


class CustomerPostgresDAO(CustomerDAO):
    def create_new_customer(self, customer: Customer) -> Customer:
        sql = "insert into customer values(default, %s, %s, %s, %s) returning customer_id"
        cursor= connection.cursor()
        cursor.execute(sql,(customer.ssn,customer.first_name,customer.last_name,customer.phonenumber))
        connection.commit()
        customer_id= cursor.fetchone()[0]
        customer.customerid = customer_id
        return customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        try:
            sql = "select * from customer where customer_id = %s"
            cursor= connection.cursor()
            cursor.execute(sql,[customer_id])
            customer_record=cursor.fetchone()
            customer= Customer(*customer_record)
            return customer
        except TypeError as e:
            return str(e)



    def update_customer(self, customer: Customer) -> Customer:
        sql = "update customer set phone_number= %s where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.phonenumber, customer.customerid))
        connection.commit()
        return customer

    def delete_customer_by_id(self, customer_id: int) -> bool:

        sql = "delete from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True


    def get_all_customers(self) -> list[Customer]:
        sql = " select * from customer"
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_list = cursor.fetchall()
        list = []
        for  customer in customer_list:
            list.append(Customer(*customer))
        return list
