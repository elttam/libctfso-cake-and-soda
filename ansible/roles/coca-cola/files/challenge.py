#!/usr/bin/env python
import sys
import random
import string
import time
import os

#FLAG = 'This is our world now... the world of the electron and the switch, the beauty of the baud. libctf{d8d07554-c34c-4944-96ae-d7e285391694} We make use of a service already existing without paying for what could be dirt-cheap if it wasn\'t run by profiteering gluttons, and you call us criminals.'
KEY = 'Nuka Cola'

def main():
  send_stream(KEY)
  sys.exit(0)

  # For generating flag and testing, comment out for prod
  #enc_flag = get_encrypted(KEY, FLAG)
  #with open('encrypted_flag', 'w') as f:
  #    f.write(enc_flag)
  #test(KEY, enc_flag)

def xor(a, b):
  return a ^ b

def send(b):
  # Hex encode byte and send
  try:
    sys.stdout.write('{:02X}\n'.format(b))
    sys.stdout.flush()
  except:
    sys.exit(1)

def get_byte():
    return random.randint(0x00, 0xff)

def send_stream(key):
  random.seed(key)
  while(1):
    time.sleep(0.001)
    send(get_byte())

def get_encrypted(key, flag):
    random.seed(key)

    # get an offset in stream
    for i in range(2121):
        b = get_byte()

    # encrypt flag with stream
    E = []
    for c in flag:
        E.append(ord(c) ^ get_byte())

    encrypted_flag = ''
    for x in E:
        encrypted_flag += '{:02x}'.format(x)
    return encrypted_flag

def test(key, encrypted_flag):
    random.seed(key)
    stream_string = ''
    for i in range(10000):
        stream_string += '{:02x}'.format(get_byte())

    KS = stream_string.decode('hex')
    E = encrypted_flag.decode('hex')

    temp_string = ''
    for i in range(0, len(KS) - len(E)):
        for j in range(0, len(E)):
            temp_string += chr(xor(ord(KS[i+j]), ord(E[j])))
        if 'libctf{' in temp_string:
            print i
            print temp_string
        temp_string = ''

if __name__ == '__main__':
  main()

