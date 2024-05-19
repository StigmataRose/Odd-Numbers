import time
import matplotlib.pyplot as plt

# Define the data
x_values = [10, 100, 1000, 10000]
times1 = [] 
times2 = []  
times3 = [] 

for value in x_values:
    max_value = value

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

  # Define the range
    start = 1
    end = max_value

    # Generate the list of odd numbers within the specified range
    odd_numbers_list = [num for num in range(start, end + 1) if num % 2 != 0]

    # Convert the list to a tuple
    odd_numbers_tuple = tuple(odd_numbers_list)

    # Create the reverse ordered tuple
    reverse_odd_numbers_tuple = tuple(reversed(odd_numbers_list))


    # start timer 3
    start_time_3 = time.time_ns()
    #---------------------------------------------------------------
    odd_numbers_3 = list(odd_numbers_tuple)
    reverse_odd_numbers_3 = list(reverse_odd_numbers_tuple)
    #---------------------------------------------------------------
    #end of timer 2
    end_time_3 = time.time_ns()
    # Calculate the elapsed time 3
    elapsed_time_3 = end_time_3 - start_time_3

    times1.append(elapsed_time_1)
    times2.append(elapsed_time_2)
    times3.append(elapsed_time_3)

    print(elapsed_time_1)
    print(elapsed_time_2)
    print(elapsed_time_3)


# Create the plot
plt.figure(figsize=(5, 5))  # Set the figure size to 500x500 pixels
plt.plot(x_values, times1, marker='o', label='Base')
plt.plot(x_values, times2, marker='s', label='2X Iter')
plt.plot(x_values, times3, marker='^', label='Hardcoded')

# Label the axes
plt.xlabel('Iterations')
plt.ylabel('Time (milli-seconds)')

# Add a title
plt.title('Odd Number Time Vs Iterations')

# Add a legend
plt.legend()

# Save the plot as a .png file
plt.savefig('plot.png', format='png', dpi=100)  # 100 DPI for 500x500 pixels

# Show the plot (optional, can be removed if only saving is required)
plt.show()
