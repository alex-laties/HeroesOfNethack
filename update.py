#!/usr/bin/python
from subprocess import call
import sys
import getopt
from random import choice
import string

repo = "git://github.com/alex-laties/HeroesOfNethack.git"

def main():
  opts = 0
  args = 0
  target = ''
  try:
    opts, args = getopt.getopt(sys.argv[1:], "t:", ["target="])
  except getopt.error, msg:
    print msg
    sys.exit(2)

  for o, a in opts:
   if o in ("-t", "--target"):
    target = a

  if target == '':
    print "no target"
    sys.exit(2)

  #make psuedo-random directory
  temp = '/tmp/'
  chars = string.letters + string.digits
  for i in range(8):
    temp = temp + choice(chars)

  print "making temp directory " + temp
  call(["mkdir", temp])
  print "cloning..."
  call(["git", "clone", repo, temp])
  print "copying..."  
  call(["cp", "-r" , temp + "/client/index.html", temp+"/client/css", temp+"/client/js", target])
  print "removing temp..."
  #call(["rm", "-rf", temp])

if __name__ == "__main__":
  main()
