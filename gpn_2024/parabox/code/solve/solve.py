
#level 1
inputs = "<Right><Right><Up><Up><Up><Up><Up><Up><Right><Right><Right>"

#level 2
inputs += "<Up><Up><Right><Right><Right><Right><Right><Up><Up><Left><Left><Left><Left><Left><Left><Up><Up><Right><Right><Right><Right><Right><Right>"

#level 3
inputs += "<Right><Right><Up><Up><Up><Up><Up><Left><Up><Right><Right><Right><Down><Left><Left><Left><Left><Left>"

#level 4
inputs += "<Down><Right><Right><Up><Up><Left><Right><Down><Down><Left><Left><Up><Up><Left><Left><Down><Left><Down><Right><Right><Left><Up><Up><Right><Right><Down><Down><Right><Down><Right><Up><Up><Down><Left><Left><Up><Up><Left><Left><Up><Up><Right><Right><Down><Up><Right><Right><Right><Down>"

#level 5
inputs += "<Right><Right><Right><Up><Up><Right><Up><Right><Up><Up><Left><Left><Left><Left><Left><Left><Left><Left><Down><Left><Left><Down><Down><Down><Down><Up><Up><Up><Up><Up><Up><Right><Right><Up><Right><Right><Right><Right><Right><Right><Right><Right>"

#level 6
inputs += "<Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Down><Left><Right><Down><Left><Down><Right><Up><Right><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Up><Right><Down><Up><Left><Right><Up><Left><Right><Down><Up><Up><Right><Left><Right><Left><Right><Left><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Left><Right><Right><Left><Right><Left><Right><Left><Right><Left><Left><Right><Left><Right><Right><Down><Down><Down><Down><Right><Right><Right><Left><Left><Left><Left><Left><Up><Down><Down><Down><Down><Down><Down><Left>"

# start 7
inputs += "<Down><Down><Up><Right><Right><Right><Up><Right><Right><Down><Left><Left><Left><Left><Down><Left><Up><Up><Up><Up>"

# prep for 8

inputs += "<Down><Up>"*40

#level 7

inputs += "<Down><Left><Down><Up><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Right>"

#level 8

# reach second save

inputs += "<Left><Right>"*32

# solve level 8
inputs += "<Left><Back><Left><Left><Up><Up><Right><Right><Right><Right><Right><Up><Right><Right><Down><Down><Right><Right><Down><Down><Left><Left><Up><Up><Up><Up><Right><Up><Up><Left><Down><Left><Down><Right><Right><Up><Right><Down><Down><Right><Down><Left><Left><Right><Up><Up><Left><Left><Down><Down><Down><Up><Right><Right><Down><Down><Left><Left><Left><Left><Up><Left><Left><Left><Left><Down><Down><Right><Right><Left><Up><Left><Up><Right><Left><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Up><Down><Right><Down><Left>"

# level 9

inputs += "<Up><Up><Up><Up><Right><Right><Right><Right><Up><Right><Right><Down><Left><Up><Left><Down><Down><Down><Down><Down><Up><Left><Left><Left><Left><Down><Down><Down><Down><Right><Right><Right><Up><Left><Left><Down><Left><Up><Up><Up><Right><Up><Right><Right><Right><Down><Down><Down><Down><Down><Up><Down><Right><Right><Right><Right><Up><Up><Up><Up><Up><Up><Right>"

# go into finish

inputs += "<Down><Down>"

inputs = inputs[1:-1].split("><")

inputs = "".join([i[0] for i in inputs])

print(inputs)
if args.LOCAL:    
    exit()

KEY_MAP = {"UP": "U", "DOWN": "D", "LEFT": "L", "RIGHT": "R", "A": "A", "B": "B", "SELECT": "S", "START": "T"}
inv_map = {v: k for k, v in KEY_MAP.items()}

print(len(inputs))
from pwn import *
import time

#context.log_level = "debug"

r = remote("the-sound-of-silence--veysel-7459.ctf.kitctf.de", "443", ssl=True)
#r = remote("localhost", "1337")

for c in inputs:
    r.sendline(inv_map[c])

r.sendline("EOF")
r.interactive()

# GPNCTF{p41n_70_d3v3l0p_h0p3fully_l355_p41n_70_50lv3_fd29a4b2833}