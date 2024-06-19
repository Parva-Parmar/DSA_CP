#!/usr/bin/env python

import os
import sys
from io import BytesIO, IOBase
from math import ceil

t = 0
def main() -> None:
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    l,r = 0,0
    
    for i in range(n):
        if(a[i] != b[i]):
            l = i
            break
    
    for i in reversed(range(n)):
        if(a[i] != b[i]):
            r = i
            break
    
    flag = 0
    for i in reversed(range(1, l+1)):
        if(b[i-1] <= b[i]):
            l-=1
            flag = 1
        else:
            flag = 0
            break
    
    if(flag):
        l=max(l-1,0)
        
    flag = 0
    for i in range(r, n-1):
        if(b[i] <= b[i+1]):
            r+=1
            flag = 1
        else:
            flag = 0
            break
    
    if(flag):
        r=min(n-1,r+1)
    print(l+1,r+1)
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