import time

for line in ["LEONARD: Hello, World!","LEONARD: Imagine, with the power of empathy, that I'm a living thing.",]:
    words = line.split(" ")
    for word in words:
        print(word, end="", flush=True)
        for longpausechar in [".","!","?"]:
            if word.endswith(longpausechar):
                time.sleep(0.5)
        for shortpausechar in [",",":",";"]:
            if word.endswith(shortpausechar):
                time.sleep(0.2)
        time.sleep(0.1)
        print(" ", end="", flush=True)  # Print space after each word
    print()  # New line after the full line
    time.sleep(1)  # Pause between lines



