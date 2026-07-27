import time


class Calculator:
    def __init__(self):
        self.__history = []


    def add(self, *args):
        total = 0

        for i in args:
            total += i

        t = time.time()
        hours, remainder = divmod(t, 3600)
        minutes, seconds = divmod(remainder, 60)

        self.__history.append({f'Add_{int(hours)}h {int(minutes)}m {int(seconds)}s' : {str(args) : total}})

        return total


    def get_history(self):
        print(self.__history)


def hello_world():
    print('Hello World')