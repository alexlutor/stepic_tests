
"""2.11 Практика по методам и свойствам (property) """
from string import  ascii_letters
from string import  ascii_lowercase



class Registration:
    __login = ''
    __password = ''

    @staticmethod
    def is_include_digit(str):
        for i in str:
            if i.isdigit():
                return True
        return False

    @staticmethod
    def is_include_only_latin(password):
        for i in password:
            if i not in ascii_letters :
                raise ValueError('Пароль должен содержать только латинский алфавит')






    def __init__(self,login, password):
        self.login = login  # передаем в сеттер login значение логин
        self.password = password  # передаем в сеттер password значение пароль






    @property
    def login(self):
        return self.__login


    @login.setter
    def login(self, login):
        """Сеттер логин"""
        if login.count('@') != 1 :
            raise ValueError("Login must include at least one ' @ '")
        if login.count('.') >= 1:
            raise ValueError("Login must include at least one ' . '")
        self.__login = login

    @property
    def password(self):
        """Геттер пароля"""
        return self.__password

    @password.setter
    def password(self, password):
        """Сеттер пароля"""
        if type(password) != str:
            raise TypeError("Пароль должен быть строкой")
        if 4 < len(password) <12 :
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')


        self.__password = password

