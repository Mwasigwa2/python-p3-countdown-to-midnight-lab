import time

def countdown(seconds):
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        seconds -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(seconds):
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        time.sleep(1)  # Pause for 1 second
        seconds -= 1
    print("HAPPY NEW YEAR!")

# Countdown without sleep
countdown(10)

# Countdown with sleep
countdown_with_sleep(10)
