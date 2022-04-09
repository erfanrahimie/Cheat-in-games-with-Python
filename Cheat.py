from pymem import *
from pymem.process import *
import keyboard

#select game and module..!
num = Pymem('wolfram.exe')
module = module_from_name(num.process_handle, 'wolfram.exe').lpBaseOfDll

#Algorithm for converting address and offsets to the current data address in Rome
def getPointer(address, offsets):
    addr = num.read_int(address)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = num.read_int(addr + offset)
    return addr + offsets[-1]

#Location of base address and offset
while True:
    if keyboard.is_pressed('F2'):
        num.write_int(getPointer(module + 0x0313D614, [0x3DC, 0x3DC, 0x3C8, 0x990]), 99999)

#MAKER : ΞRFAN