#!/usr/bin/python3

def uppercase(s):
    print("".join(chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c for c in s))
