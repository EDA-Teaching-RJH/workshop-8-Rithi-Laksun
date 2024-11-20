import pytest 
from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide

def main():
    test()
    test1()
    test2()
    test3()

def test():
    try:
        assert add(1,2) == 3
    except (AssertionError , NameError):
        print("a + b not equal to 3.")
def test1():
    try:
        assert subtract(4,2) == 2
    except (AssertionError, NameError):
        print("a - b not equal to 2.")
def test2():
    try:
        assert multiply(1,2) == 2
    except (AssertionError, NameError):
        print("a x b not equal to 2.") 
def test3():
    try:
        assert divide(1,2) == 0.5
    except (AssertionError, NameError):
        print("a / b not equal to 0.5.")

if __name__ == "__main__":
    main
