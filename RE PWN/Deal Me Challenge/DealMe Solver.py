import subprocess
import time
import os
import random
import concurrent.futures

# Define the command to run the executable
command = r"C:\Users\deady\OneDrive\Desktop\DealMe.exe"

# Define the inputs to send to the process
inputs = "\n" * 4

# Initialize the retry counter
max_retries = 1000000
retries = 0

# Define the number of concurrent threads
num_threads = 4

# Function to execute the subprocess
def play_game():
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    input_str = '\n'.join(inputs[:5])
    output, _ = process.communicate(input_str.encode('utf-8'))

    # Count the number of wins
    wins = 0
    for line in output.decode('utf-8').split('\n'):
        if 'Win' in line:
            wins += 1

    return wins, output.decode('utf-8')

# Start the process and communicate with it using the inputs
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = {executor.submit(play_game): i for i in range(max_retries)}
    for future in concurrent.futures.as_completed(futures):
        retries += 1

        # Get the output
        wins, output = future.result()
        # Print the output
        print(output)

        if "cygame{" in output:
            with open(r"C:\Users\deady\OneDrive\Desktop\DealMeLogs.txt", 'a') as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Attempt: {retries}, Wins: {wins}\n")
                f.write(output)
            # If the flag is found, cancel all other threads and break out of the loop
            print("We Did it, you Won!")
            print(output.decode('utf-8'))
            for pending_future in futures:
                pending_future.cancel()
            break

if retries >= max_retries:
    print("Reached maximum retries without success.")