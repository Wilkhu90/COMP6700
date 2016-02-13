import math

def calc(number):

    if number < 2: 
        return []
    number = number + 1
    
    # CITATION: Sieve of Eratosthenes
    # Create list of all numbers up to max
    # Start with first prime
    # Strike all multiples 
    # repeat for next un-struck number in list
    
    # set up initial matrix
    isPrimeList = generateNumberList(number)
    
    #Striking off multiples from the list
    checkListForMultiples(number, isPrimeList)

    #Create final list of output prime numbers.
    resultPrimeNumbers = createPrimeNumberList(number, isPrimeList)
      
    return resultPrimeNumbers

def generateNumberList(number):
    return [False, False] + [True] * (number - 2)

def checkListForMultiples(number, isPrimeList):
    for indexItem in range(2, int(math.sqrt(number) + 1)):
        if isPrimeList[indexItem]:
            for multiples in range(2 * indexItem, number, indexItem):
                isPrimeList[multiples] = False


def createPrimeNumberList(number, isPrimeList):
    primeNumbers = []
    for indexNumber in range(0, number):
        if isPrimeList[indexNumber]:
            primeNumbers.append(indexNumber)
    return primeNumbers