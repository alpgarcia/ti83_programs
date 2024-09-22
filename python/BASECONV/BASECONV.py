

def read_number():
  n=input("> ")
  return n

def to_bin(d: int):
  b = "{0:016b}".format(d)
  return ' '.join([
    b[i:i+4]
    for i in range(0,
                   len(b),
                   4)])

def to_hex(d: int):
  h = "{0:04x}".format(d)
  return "   " + "    ".join(h)

def show(i: int):
  print("{:19d}".format(i))
  print(to_hex(i))
  print(to_bin(i))


def convert(n: str):
  s = u"" + n.strip().lower()
  i = int(s, 0)
  show(i)


while True:
  try:
    n = read_number()
    if n == "q":
      break
      
    else:
      convert(n)
      
  except:
    print("Unsupported. Try again")