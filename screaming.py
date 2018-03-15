# coding=utf-8
import sys

newfileName = sys.argv[1].split(".")[0]

newfile = open(newfileName+".bf","w+")

with open(sys.argv[1]) as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if c == "á":
      newfile.write("<")
    elif c == "à":
      newfile.write(">")
    elif c == "A":
      newfile.write("+")
    elif c == "a":
      newfile.write("-")
    elif c == "â":
      newfile.write(".")
    elif c == "ã":
      newfile.write(",")
    elif c == "Á":
      newfile.write("[")
    elif c == "À":
      newfile.write("]")
    else:
      newfile.write(c)
