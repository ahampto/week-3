import seaborn as sns
import pandas as pd


# update/add code below ...
def fib(n):
    """ Return the nth Fibonacci number. """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def to_binary(n):
    """ Return the binary representation of a non-negative integer n as a string. """
     # Base case
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        to_binary(n // 2) + str(n % 2)

        # return to_binary(n // 2) + str(n % 2)

def task1():
    """ Load the dataset and return the number of missing values in each column, sorted in descending order. """
    return df.isna().sum().sort_values()
    

def task2():
    """ Return a DataFrame with the total number of admissions per year. """
    return df.groupby('year').agg(total_admissions=('year', 'count'))
    print('data needed some cleaning, including renaming and dropping columns as well as converting data types')

def task3():
    """ Return a DataFrame with the average age of patients grouped by """

    return df.groupby('gender')['age'].mean()
    print('Some cleaning had to be done, including removing rows with different genders and converting ages to numeric values.')


def task4():
    """ Return a Series with the top 5 most common professions among patients. """
    return df['profession'].value_counts()[:5].index.tolist()