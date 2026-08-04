import time


def hello_world():
    print('Hello World')


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


if __name__ == '__main__':
    # only when I run python calculator.py, run below code
    hello_world()

    c = Calculator()
    
    c.add(1, 2, 2)
    c.add(1, 2, 2, 100)
    c.add(1, 2, 2, 17392193)
    c.add(1, -90, 2)

    c.get_history()