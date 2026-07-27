# importing default or built-in python modules
import sys

# importing custom and project specific python package and entities
from utils import StorePPS, InvalidAmountError, InsufficientStoreBalance


spps = StorePPS()

while True:
    print('~' * 50)
    print('Welcome to Store Payment Processing System')
    print('-' * 50)
    print('Press 1 for Add cash to the system')
    print('Press 2 to Refund the money')
    print('Press 3 to Show current available balance')
    print('Press 4 to Check the transaction history')
    print('Press 5 to Exit the system')
    print('~' * 50)

    try:
        choice = int(input('\nEnter your choice (1-5): ').strip())

        payment_method = {1: 'Credit Card', 2: 'UPI'}

        if choice == 1:
            print('Press 1 to use Credit Card Payment method')
            print('Press 2 to use UPI Payment method')

            payment_choice = int(input('Enter your payment method choice (1-2): ').strip())

            if (payment_choice in payment_method.keys()):
                payment_method_type = payment_method[payment_choice]
            else:
                print('Invalid payment method selected.')
                continue

            amount = float(input('Enter the amount to add: ₹ ').strip())
            spps.add_cash(payment_method_type, amount)

        elif choice == 2:
            refund_amount = float(input('Enter the amount to refund: ₹ ').strip())
            spps.refund_amount(refund_amount)

        elif choice == 3:
            spps.show_balance()

        elif choice == 4:
            print('Please find the Transaction History for the day\n')
            spps.check_transaction_history()

        elif choice == 5:
            print('\nExiting the System.\n')
            sys.exit()

        else:
            print('\nInvalid choice! Please select a number between 1 and 5.')
    
    except ValueError:
        print("\nError: Invalid input type! Please enter numeric values only.")

    except (InvalidAmountError, InsufficientStoreBalance) as payment_exception:
        print(f'\n{payment_exception}')

    except Exception as e:
        print(f'\nAn unexpected error occured : {e}')