import itertools
import string
import time

chars = string.printable

while True:
    password = input("Input a Password with a maximum length of 10: ")

    if len(password) <= 10:
        break  
    else:
        print("Password length cannot exceed 10 characters. Please try again.")

max_length = 10
start_time = time.time()

for length in range(1, max_length + 1):
    for combination in itertools.product(chars, repeat=length):
        candidate = "".join(combination)
        print("Trying password:", candidate)
        if candidate == password:
            end_time = time.time()
            print("Password found:", candidate)
            time_taken = end_time - start_time
            print("Time taken:", time_taken, "seconds")
            raise SystemExit
