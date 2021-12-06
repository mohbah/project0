from abc import abstractmethod, ABC

from entities import Customer


class CustomerService(ABC):
    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_all_customers(self) -> list[Customer]:
        pass

    @abstractmethod
    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        pass

    @abstractmethod
    def service_update_customer(self, customer: Customer) -> Customer:
        pass
