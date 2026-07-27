from abc import ABC, abstractmethod         # importing default or built-in python modules


# Abstraction
# creating an abstract class PaymentProcessingSystem which inherits the Abstract Base Class (ABC)
class PaymentProcessingSystem(ABC):

    # declaring or defining abstract methods (these are highly defined) which should be necessarily defined properly in the child class inheriting the abstract class

    @abstractmethod         # decorator
    def __init__(self) -> None:
        pass

    @abstractmethod         # decorator
    def add_cash(self, payment_type: str, cash_amount: float) -> None:
        pass

    @abstractmethod         # decorator
    def refund_amount(self, refund_amount: float) -> None:
        pass

    @abstractmethod         # decorator
    def show_balance(self) -> None:
        pass

    @abstractmethod         # decorator
    def check_transaction_history(self) -> None:
        pass