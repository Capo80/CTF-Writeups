from pwn import *


KEY_MAP = {"UP": "U", "DOWN": "D", "LEFT": "L", "RIGHT": "R", "A": "A", "B": "B", "SELECT": "S", "START": "T"}

try:
    print("Please provide the inputs (UP, DOWN, LEFT, RIGHT, A, B, SELECT, START) line by line and end with an EOF")
    inputs = ""
    for _ in range(0x1000):
        line = input("").strip()
        if line == "EOF":
            break
        elif line.startswith("#") or len(line) == 0:
            continue
        else:
            inputs += KEY_MAP[line.upper()]

    p = process(["/home/ctf/gearboy/platforms/linux/gearboy", "parabox.gbc", inputs], stderr=open("/dev/null", "w+b"))
    p.interactive()

except Exception as e:
    print("Something went wrong: %s" % e)
    exit(-1)