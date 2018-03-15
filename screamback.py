# coding=utf-8
import sys

newfileName = sys.argv[1].split(".")[0]

newfile = open(newfileName+".scream","w+")

with open(sys.argv[1]) as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if c == "<":
      newfile.write("á")
    elif c == ">":
      newfile.write("à")
    elif c == "+":
      newfile.write("A")
    elif c == "-":
      newfile.write("a")
    elif c == ".":
      newfile.write("â")
    elif c == ",":
      newfile.write("ã")
    elif c == "[":
      newfile.write("Á")
    elif c == "]":
      newfile.write("À")
    else:
      newfile.write(c)
