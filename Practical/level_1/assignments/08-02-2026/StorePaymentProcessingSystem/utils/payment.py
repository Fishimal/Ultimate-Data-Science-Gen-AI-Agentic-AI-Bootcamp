import random       # importing default or built-in python module


# All the print messages are for the customer

# object of this class is instantiated when a person opts to pay via credit card
class CreditCardPayment:
    def __init__(self) -> None:
         pass
    
    # Run-time Polymorphism
    def add_cash(self, amount: float) -> None:
        print(f'Your bill amount : ₹ {amount:.2f}')
        print('Swipe your credit card')

        # creating a random card_number as presently the problem statement is only for the Store Payment Processing System and it is not focussing on the Customer entity
        # Securing the variable so that it is not used outside the class
        __card_number = str(random.choice(range(0, 9999))).zfill(4)

        print(f'An amount of ₹ {amount:.2f} has been debited from your credit card {__card_number:X>16}')


# object of this class is instantiated when a person opts to pay via upi
class UPIPayment:
    def __init__(self) -> None:
        pass

    # Run-time Polymorphism
    def add_cash(self, amount: float) -> None:
        print(f'Your bill amount : ₹ {amount:.2f}')
        print('Scan the QR code')

        # creating a random account_number as presently the problem statement is only for the Store Payment Processing System and it is not focussing on the Customer entity
        # Securing the variable so that it is not used outside the class
        __account_number = str(random.choice(range(0, 9999))).zfill(4)
    
        print(f'An amount of ₹ {amount:.2f} has been debited from your SB Account {__account_number:X>18} via UPI transaction')