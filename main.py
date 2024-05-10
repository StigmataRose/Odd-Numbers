#For the record I did not use chatgpt for this
odd_numbers = []

isOdd = True

for i in range(1,100):
    if isOdd: 
        odd_numbers.append(i)
    
    isOdd = not isOdd


print(odd_numbers)