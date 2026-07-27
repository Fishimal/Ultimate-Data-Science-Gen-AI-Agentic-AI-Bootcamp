import random       # importing default or built-in python module


class PaymentSystemError(Exception):
    """Base class for all payment system exceptions."""
    pass


class InvalidAmountError(PaymentSystemError):       # Multi-level Inheritance
    def __init__(self, amount: float) -> None:
        self.amount = amount

        # passing the exception message to the base class (Exception) so that it catches the exception and displays the exception message without any error
        super().__init__(f'Invalid amount : Bill amount should be greater than 0.\nEntered amount : ₹ {self.amount:.2f}')


class InsufficientStoreBalance(PaymentSystemError):       # Multi-level Inheritance
    def __init__(self, refund_amount: float) -> None:
        self.refund_amount = refund_amount

        # creating a random user_account_number as presently the problem statement is only for the Store Payment Processing System and it is not focussing on the Customer entity
        # Securing the variable so that it is not used outside the class
        __user_account_number = str(random.choice(range(0, 9999))).zfill(4)

        # passing the exception message to the base class (Exception) so that it catches the exception and displays the exception message without any error
        super().__init__(f'Refund amount exceeds the current available balance.\nA refund of ₹ {self.refund_amount:.2f} will be processed to your SB account {__user_account_number:X>18} within a few days.')