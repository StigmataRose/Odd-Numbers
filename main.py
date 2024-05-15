import time

max_value = 100

# start timer 1
start_time_1 = time.time_ns()
#---------------------------------------------------------------
odd_numbers_1 = []
is_odd = True
for i in range(1,max_value):
    if is_odd: 
        odd_numbers_1.append(i)
    
    is_odd = not is_odd

reverse_odd_numbers_1 = odd_numbers_1[::-1]
#---------------------------------------------------------------
#end of timer 1
end_time_1 = time.time_ns()
# Calculate the elapsed time
elapsed_time_1 = end_time_1 - start_time_1


# start timer 2
start_time_2 = time.time_ns()
#---------------------------------------------------------------
odd_numbers_2 = []
reverse_odd_numbers_2 = []
for i in range(1,max_value,2):
    odd_numbers_2.append(i)
    reverse_odd_numbers_2.append(max_value-i)
#---------------------------------------------------------------
#end of timer 2
end_time_2 = time.time_ns()

# Calculate the elapsed time
elapsed_time_2 = end_time_2 - start_time_2
print("Elapsed time (Approach 1):", elapsed_time_1, "nano-seconds")
print("Elapsed time (Approach 2):", elapsed_time_2, "nano-seconds")
percent_increase = (elapsed_time_2 / elapsed_time_1) * 100
print("Percent Increase: ", round(percent_increase,2), " %")