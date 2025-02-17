

def to_binary_list(n):
  result = []
  while n != 0:
      result.append(n % 2)
      n = n // 2
  result.reverse()
  return result

def from_binary_list(bits):
    result = 0
    for b in bits:
        result = result * 2 + b
    return result

def padzero(list):
    return [0] * (8 - len(list)) + list

def encode_string(l):
    result = []
    for c in l:
        result = result + padzero(to_binary_list(ord(c)))
    return result

def decode_string(bits):
    result = ""
    for i in range(0,len(bits)//8):
        chunk = bits[i*8:(i+1)*8]
        print(chunk, chr(from_binary_list(chunk)))
        result = result + chr(from_binary_list(chunk))
    return result

encoded_message = [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0]

# [0, 1, 1, 0, 1, 0, 0, 0] h
# [0, 1, 1, 0, 0, 1, 0, 1] e
# [0, 1, 1, 0, 1, 1, 0, 0] l
# [0, 1, 1, 0, 1, 1, 0, 0] l
# [0, 1, 1, 0, 1, 1, 1, 1] o
# [0, 0, 1, 0, 0, 0, 0, 0]  
# [0, 1, 1, 1, 0, 1, 1, 1] w
# [0, 1, 1, 0, 1, 1, 1, 1] o
# [0, 1, 1, 1, 0, 0, 1, 0] r
# [0, 1, 1, 0, 1, 1, 0, 0] l
# [0, 1, 1, 0, 0, 1, 0, 0] d

print(decode_string(encoded_message))

# print(encode_string("hello world"))
        
# for i in range(0,256):
#     print(padzero(to_binary_list(i)))
#     print(chr(i))
#     print(from_binary_list(padzero(to_binary_list(i))))
