

import sys
import subprocess


with open(sys.argv[1]) as oldFiles:
  oldLine=oldFiles.readline().strip()
  while oldLine != "":
    # newLine=oldLine
    newLine=oldLine.replace("jane", "jdoe")
    print("{} -> {}".format(oldLine,newLine))
    subprocess.run(["mv", oldLine, newLine])
    oldLine=oldFiles.readline()
