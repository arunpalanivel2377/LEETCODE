"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""

def fib(n: int) -> int:
        if n <=1:
            print(n)
        a,b = 0,1
        for _ in range(2,n+1):
            a,b = b,a+b
        print(b)

fib(3)