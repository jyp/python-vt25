

def to_binary_string(n):
  result = ""
  while n != 0:
      if (n % 2) == 1:
          result = "1" + result
      else:
          result = "0" + result
      n = n // 2
  return result

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

for i in range(0,100):
    print(from_binary_list(padzero(to_binary_list(i))))
