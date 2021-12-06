from abc import ABC, abstractmethod

from entities.Customer import Customer
from entities.Account import Account


class CustomerDAO(ABC):
    @abstractmethod
    def create_new_customer(self, customer : Customer)->Customer:
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id : int)-> Customer:
        pass

    @abstractmethod
    def update_customer(self, customer: Customer)-> Customer:
        pass

    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass

    @abstractmethod
    def get_all_customers(self) -> list[Customer]:
        pass




