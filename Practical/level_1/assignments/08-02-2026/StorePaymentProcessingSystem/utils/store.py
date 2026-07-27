# importing default or built-in python modules
import random
from datetime import datetime
from zoneinfo import ZoneInfo

# importing custom and project specific python modules
from .pps import PaymentProcessingSystem
from .payment import CreditCardPayment, UPIPayment
from .datetimeformatter import FormatTransactionDateTime
from .exception import *


class StorePPS(PaymentProcessingSystem):        # Multi-level Inheritance & Abstraction
    # initialising the required variables or objects
    def __init__(self) -> None:
        # encapsulation
        self.__balance = 1000.00        # private variable --> initialising the store balance with a minimum amount
        self.__transaction_history = {}     # private variable


    # method to add cash to the POS
    def add_cash(self, payment_type: str, cash_amount: float) -> None:
        if (cash_amount <= 0):
            raise InvalidAmountError(cash_amount)       # raising custom exception or error

        # run-time polymorphism
        if payment_type.lower() == 'credit card':
            CreditCardPayment().add_cash(cash_amount)
        else:
            UPIPayment().add_cash(cash_amount)

        # updating the store balance after adding cash to the POS
        self.__balance += cash_amount

        # recording the date and time at which the transaction is done
        add_cash_time = datetime.now(ZoneInfo("Asia/Kolkata"))

        # formatting the date and time in a presentable manner
        formatted_date, formatted_time = FormatTransactionDateTime.format_date_time(add_cash_time)

        # updating the transaction history after adding cash to the POS
        self.__transaction_history[(formatted_date, formatted_time)] = {
            'Transaction' : 'Cash added to POS',
            'Payment Type' : payment_type,
            'Credited Amount' : f'₹ {cash_amount:.2f}',
            'Available Balance' : f'₹ {self.__balance:.2f}'
        }


    # method to refund amount to the customer
    def refund_amount(self, refund_amount: float) -> None:
        if (refund_amount <= 0):
            raise InvalidAmountError(refund_amount)         # raising custom exception or error

        if (refund_amount > self.__balance):
            raise InsufficientStoreBalance(refund_amount)           # raising custom exception or error

        # creating a random user_account_number as presently the problem statement is only for the Store Payment Processing System and it is not focussing on the Customer entity
        # Securing the variable so that it is not used outside the class
        __user_account_number = str(random.choice(range(0, 9999))).zfill(4)

        # updating the store balance after adding cash to the POS
        self.__balance -= refund_amount

        # following message is for the customer
        print(f'A refund of ₹ {refund_amount:.2f} has been credited to your SB account {__user_account_number:X>18} via NEFT')

         # recording the date and time at which the transaction is done
        refund_amount_time = datetime.now(ZoneInfo("Asia/Kolkata"))

        # formatting the date and time in a presentable manner
        formatted_date, formatted_time = FormatTransactionDateTime.format_date_time(refund_amount_time)

        # updating the transaction history after refunding to the customer
        self.__transaction_history[(formatted_date, formatted_time)] = {
            'Transaction' : 'Refund to Customer',
            'Debited Amount' : f'₹ {refund_amount:.2f}',
            'Available Balance' : f'₹ {self.__balance:.2f}'
        }


    # method to display the current available balance of the store
    def show_balance(self) -> None:
        print(f'Store\'s current available balance : ₹ {self.__balance:.2f}')


    # method to display the transaction history of the store in a presentable manner
    def check_transaction_history(self) -> None:
        # if someone checks the transaction history at the start of the day
        if (len(self.__transaction_history) == 0):
             print('No transactions till now')
             self.show_balance()

        # this part will show the transaction history throughout the day
        else:
            for transaction_date_time in self.__transaction_history:
                print(f'Transaction on {transaction_date_time[0]} at {transaction_date_time[-1]}')

                for key, value in self.__transaction_history[transaction_date_time].items():
                    print(f'{key:>20} : {value}')

                print('\n')