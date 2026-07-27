from datetime import datetime       # importing default or built-in python module


# this module is created to format the exact day and time at which each transactions are happening
class FormatTransactionDateTime:
    
    @staticmethod
    def format_date_time(transaction_date_time: datetime) -> tuple[str, str]:
        date, time = str(transaction_date_time).split()
        index = time.find('.')
        time = time[:index]

        return (date, time)