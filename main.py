import os
import sys
import time
import colorama # type: ignore
from colorama import* # type: ignore
from os import*

cpu = 'I3core'
ram = 932
gpu = 932

bits = 16

print("Booting from a disk...")
print("cpu = I3core")
print("ram = 932 gb")
print("gpu = 932")

player1 = input("$>")

if player1 == "kernel":
    time.sleep(2.0)
    print("Hello World")
    print("Good Bye World")

player1 = input("name:")
input("password:")

print("Hello " + player1)

print("Welcome To 16 bits kernel.")

while True:
    input("$> ")
    print("Kernel is cancelled")