
import unittest
from FA04.Sieve.prod.Sieve import calc, generateNumberList, checkListForMultiples, createPrimeNumberList


class SieveTest(unittest.TestCase):


    def test001(self):
        x = int(raw_input("input a value "))    
        print "The primes are "
        print calc(x)

    def test002(self):
        numberList = generateNumberList(10)
        secondList = [False, False, True, True,True, True, True, True,True, True]
        self.assertEqual(numberList, secondList)
    
    def test003(self):
        numberList = generateNumberList(10)
        checkListForMultiples(10, numberList)   
        secondList = [False, False, True, True, False, True, False, True, False, False]
        self.assertEqual(numberList, secondList)
        
    def test004(self):
        numberList = generateNumberList(10)
        checkListForMultiples(10, numberList)   
        primesList = createPrimeNumberList(10, numberList)
        secondList = [2, 3, 5, 7]
        self.assertEqual(primesList, secondList)    