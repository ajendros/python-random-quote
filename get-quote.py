import random
import sys

def writeQuotes():
  f = open("python-random-quote\quotes.txt", "a")
  f.write(sys.stdin.readline())
  f.close()

def main():
  f = open("python-random-quote\quotes.txt", "r")
  quotes = f.readlines()
  f.close()

  last=len(quotes)
  rnd = random.randint(0,last)
  print(quotes[rnd].rstrip())
  
  rnd = random.randint(0,last)
  print(quotes[rnd].rstrip())
  
if __name__== "__main__":
  writeQuotes()
  main()
