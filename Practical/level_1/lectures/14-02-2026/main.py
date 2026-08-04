from my_module import test_1, a

print(__name__)

'''
    __name__ is a special variable
    python maintains it internally
    it has its execution file name in it
    if __name__ is present in the same file you are executing from, then __name__ == '__main__'
    if __name__ is not present in the current file you are executing from, then __name__ == that file name
'''