def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

s = input("Input bit stream: ")

print(bitstring_to_bytes(s))


binary = []
def bytes_to_bitstring(s_str):
	for s in s_str:
	        binary.append(bin(ord(s)))
s_str = input("String: ")
bytes_to_bitstring(s_str)

b_str = ''.join(str(b_str) for b_str in binary)

print(b_str.replace('b',''))

def bytes_to_bits(hi):
    for b in byteStr:
        yield b&1
        b>>=1
        print(b)

print(bytes_to_bits("0x104d3f1f8"))

def bits_to_bytes(bitStr):
    s,i=0
    for b in bitstr:
        s =(s>>1)|(0,0xff)[b]
        i+=1
        if i ==8:
            yield s
    while i <8:
        s>>=1
        i+=1
        yield s

print(bits_to_bytes("0110100001100101011011000110110001101111"))
