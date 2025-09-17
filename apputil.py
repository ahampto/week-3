import seaborn as sns
import pandas as pd


# update/add code below ...
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        to_binary(n // 2) + str(n % 2)

        return to_binary(n // 2) + str(n % 2)

def task1():
    return df.isnull().sum().sort_values(ascending=False)
    

def task2():
    return df.groupby('year').agg(total_admissions=('year', 'count'))
    print('data needed some cleaning, including renaming and dropping columns as well as converting data types')

def task3():
    return df.groupby('gender')['age'].agg(['mean'])
    print('Some cleaning had to be done, including removing rows with different genders and converting ages to numeric values.')


def task4():
    return df['profession'].value_counts()[:5]