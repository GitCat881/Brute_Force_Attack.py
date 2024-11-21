import time
import string
import itertools

#Step 1: Ask the user to input a password
password = input("Enter a password to test: ")

#Step 2: Define the possible characters
characters = string.ascii_letters + string.digits

#Step 3: Initialize variable
found = False
attemps = 0
start_time = time.time()

# Step 4: Start the brute force process
print("Starting brute force attack...")
for length in range(1,len(password)+1): # incrementing the length
    for attemp in itertools.product(characters,repeat=length): # Generate 
        attemps +=1
        attemp_password =''.join(attemp) # Convert tuple to string
        if attemp_password == password:
            found = True
            break
    if found:
        break

# Step 5: Calculate duration 
end_time = time.time()
duration = end_time - start_time

# Step 6: Display the result
print("Password found: ", attemp_password)
print("Number of attemps: ", attemps)
print("Total time taken: ", duration)