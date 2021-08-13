#!/usr/bin/python3

from custom_lib import fact, anagram
import timeit, functools

def py_fact(n):
    if (n < 0):
        return 0
    if (n == 0):
        return 1
    else:
        return n * fact(n-1)

def py_anagram(str1,str2):
    length = len(str1)
    if(length == len(str2)):
        for i in str1:
            found = False
            for j in str2:
                if(i == j):
                    found = True
                    break
        if found:
            return False
        else:
            return True
    else:
        return False

def benchmark():
    fact_number = 20
    repetitions = 30000000
    
    print("Factorial benchmark:")
    c_time = timeit.Timer(functools.partial(fact, fact_number)).timeit(repetitions)
    py_time = timeit.Timer(functools.partial(py_fact, fact_number)).timeit(repetitions)
    print(f"{c_time=}\n{py_time=}")

    print("Anagram benchmark:")
    c_time = timeit.Timer(functools.partial(anagram, "nonuniversalist", "involuntariness")).timeit(repetitions)
    py_time = timeit.Timer(functools.partial(py_anagram, "nonuniversalist", "involuntariness")).timeit(repetitions)
    print(f"{c_time=}\n{py_time=}")

if __name__=="__main__":
    benchmark()
