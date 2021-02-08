from random import randint
n = int(input())
numbers = []
for i in range(n):
    k = int(input())
    numbers.append(k)
#print("numbers",numbers)
copyNumbers = numbers.copy()
copyNumbers.sort()
sortedNumbers = copyNumbers.copy()
#print("sorted",sortedNumbers)

while (numbers!=sortedNumbers):
    i = randint(0,n-1)
    j = randint(0,n-1)
    if (numbers[i]>numbers[j]):
        copy = numbers[j]
        numbers[j] = numbers[i]
        numbers[i] = copy
    #print("Randomly sorting...",numbers)
#print("Sorted finally. yay! ")
for k in range(n-1):
    print(numbers[k],end=' ')
print(numbers[n-1],end='')
