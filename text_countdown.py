from sense_emu import SenseHat
from time import sleep
sense_emulator = SenseHat()
G = [0, 255, 0]

i = 9
for i in range(9, 0, -1):
    
    sense_emulator.show_letter(f'{i}', G)
    
    sleep(1)
    G[0] += 20
    G[1] -= 20
    
    
P = [255, 0, 255]
sense_emulator.show_letter('0', P)
