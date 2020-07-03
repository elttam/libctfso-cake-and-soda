#!/usr/bin/env python
import sys
import random
import select

#FLAG = 'We explore... and you call us criminals. We seek after knowledge... and you call us criminals. We exist without skin color, without nationality, without religious bias... and you call us criminals. libctf{2946adf1-cd78-4346-8b07-aa84c8cf7279} You build atomic bombs, you wage wars, you murder, cheat, and lie to us and try to make us believe it\'s for our own good, yet we\'re the criminals.'
KEY = 'Orange Bomb'

def main():
  random.seed(KEY)

  r = receive()
  e = encrypt(KEY, r)
  send(e)
  sys.exit(0)

  # For generating flag and testing, comment out for prod
  #test(KEY, FLAG)

def receive():
  # Ten second timer for user to respond
  rlist, wlist, xlist = select.select([sys.stdin], [], [], 10)
  if rlist:
    try:
      # Remove newline and return
      r = sys.stdin.readline().replace('\n','')
      return r
    except:
      sys.exit(1)
  else:
    sys.exit(1)

def send(s):
  try:
    sys.stdout.write('{}\n'.format(s))
    sys.stdout.flush()
  except:
    sys.exit(1)

def encrypt(key, s):
    # encrypt with stream
    enc_bytes = []
    for c in s:
        enc_bytes.append(xor(ord(c), get_byte()))
    # return hex string
    enc_string = ''
    for b in enc_bytes:
        enc_string += '{:02x}'.format(b)
    return enc_string

def get_byte():
    return random.randint(0x00, 0xff)

def xor(a, b):
    return a ^ b

def test(key, flag):
  # Get an offset in keystream
  for i in range(2351):
    get_byte()

  # Encrypt flag
  enc_flag = encrypt(key, flag)
  with open('encrypted_flag', 'w') as f:
      f.write(enc_flag)

  # Encrypt plaintext
  random.seed(key)
  pt = 'a' * 10000
  enc_pt = encrypt(key, pt)

  # Try decrypt at each offset
  Ef = enc_flag.decode('hex')
  Ept = enc_pt.decode('hex')

  for i in range(0, len(pt) - len(Ef)):
    temp = ''
    for j in range(0, len(Ef)):
      temp += chr(xor(xor(ord(Ept[i+j]), ord(Ef[j])), ord(pt[i+j])))
    if 'libctf{' in temp:
      print 'Match at stream offset: {}'.format(str(i))
      print temp

if __name__ == '__main__':
  main()

