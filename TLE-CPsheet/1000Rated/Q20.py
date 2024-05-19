#!/usr/bin/env python

'''
https://codeforces.com/problemset/problem/1567/B
'''
import os
import sys
from io import BytesIO, IOBase
from math import ceil

def computeXOR(n:int) -> int : 
  
    # Modulus operator are expensive  
    # on most of the computers. n & 3  
    # will be equivalent to n % 4. 
  
    # if n is multiple of 4  
    if n % 4 == 0 : 
        return n 
  
    # If n % 4 gives remainder 1 
    if n % 4 == 1 : 
        return 1
  
    # If n%4 gives remainder 2  
    if n % 4 == 2 : 
        return n + 1
  
    # If n%4 gives remainder 3 
    return 0
        
t = 0
def main() -> None:
    a, b = map(int, input().split())
    
    xor = computeXOR(a - 1)
    ans = a
        
    if xor == b:
        print(ans)
    else:
        if xor ^ b == a:
            print(ans + 2)
        else:
            print(ans + 1)
    return



# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    if(t == 0):
        t = int(input())
    for loop in range(t):
        main()