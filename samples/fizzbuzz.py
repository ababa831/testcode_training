# -*- coding: utf-8 -*-
class FizzBuzz(object):
    
    def __init__(self):
        pass
    
    def __is_fizz(self, num):
        if num % 3 == 0:
            return True
        return False
    
    def __is_buzz(self, num):
        if num % 5 == 0:
            return True
        return False
    
    def __is_fizz_buzz(self, num):
        if self.__is_fizz(num) and self.__is_buzz(num):
            return True
        else:
            False

    def judge(self, num):
        if self.__is_fizz_buzz(num):
            return "FizzBuzz"
        elif self.__is_fizz(num):
            return "Fizz"
        elif self.__is_buzz(num):
            return "Buzz"

        return num