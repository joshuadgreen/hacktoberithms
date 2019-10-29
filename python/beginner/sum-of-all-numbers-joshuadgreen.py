def sum_of_all_numbers(numList):
    numSum = 0
    for i in range(min(numList),max(numList)+1):
        numSum += i
    return numSum
