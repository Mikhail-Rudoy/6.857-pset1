def ascii_word(string):
  output = []
  for char in string:
    output.append(ord(char))
  return output


def xor_word(array1, array2):
  output = []
  for i in xrange(len(array1)):
    output.append(array1[i] ^ array2[i])
  return output

def main():
  c1 = [0xe9, 0x3a, 0xe9, 0xc5, 0xfc, 0x73, 0x55, 0xd5]
  c2 = [0xf4, 0x3a, 0xfe, 0xc7, 0xe1, 0x68, 0x4a, 0xdf]
  result = xor_word(c1, c2)
  # str rep of ascii bytes
  resultstr = ''.join([str(x) for x in result])

  f = open('words.txt', 'r')
  words = []
  for line in f.readlines():
    words.extend(line.strip().split(' '))

  # find 2 words such that w1 ^ w2 == result
  # put result ^ w into hashtable => result ^ w1 = w2
  hashtable = {}
  for i in xrange(len(words)):
    m2 = ''.join([str(x) for x in xor_word(result, ascii_word(words[i]))])
    hashtable[m2] = words[i]

  for i in xrange(len(words)):
    ascii_str = ''.join([str(x) for x in ascii_word(words[i])])
    if ascii_str in hashtable:
      print "found match:"
      print hashtable[ascii_str]
      print words[i]
      break
  return

if __name__ == "__main__":
  main()
