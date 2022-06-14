import os
name = "Dir1"
os.mkdir(f"{os.getcwd()}/{name}")
os.mkdir(f"{os.getcwd()}/{name}/Dir2")
os.mkdir(f"{os.getcwd()}/{name}/Dir3")
os.mkdir(f"{os.getcwd()}/{name}/Dir3/Dir4")
f = open("File.txt", "w")
