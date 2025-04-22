import time

for line in ["LEONARD: Hello, World!","LEONARD: Imagine, with the power of empathy, that I'm a living thing.",]:
    for char in line:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(1)



