import pytest
import math
def findsum(num):
    return num*(num+1)/2
def test_findsum():
    assert findsum(5)==15
def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)
def test_factorial():
    assert factorial(5)==120
l=[]
def printDivisors(n):
    i=1
    while i<=n:
        if(n%i==0):
            l.append(i)
        i=i+1
    return (l)
# printDivisors(100)
l1=[1, 5]
def test_printDivisors():
    assert printDivisors(5)==l1