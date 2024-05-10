#For the record I did not use chatgpt for this
odd_numbers = []

is_odd = True

for i in range(1,100):
    if is_odd: 
        odd_numbers.append(i)
    
    is_odd = not is_odd

def reverseList(lst):
    return lst[::-1]

print("Odd Numbers")
print(odd_numbers)

print("Reversed Odd Numbers")
reverse_odd_numbers = reverseList(odd_numbers)
print(reverse_odd_numbers)