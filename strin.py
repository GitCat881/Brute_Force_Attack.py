#import binascii


#Hex_string = "pghbvsdppqze8+"
#Float = float("!f", binascii.unhexlify(Hex_string))[0]
#print(Float)

#import struct

#Hex_string = "pghbvsdppqze8+"
#Float = struct.unpack("!f", binascii.unhexlify(Hex_string))[0]
#print(Float)

test = "1325"
def is_num(v):
    num = input("v")
    if num.isdigit():
        return num
    else:
        print("no")
