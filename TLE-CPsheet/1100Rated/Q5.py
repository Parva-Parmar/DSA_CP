#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
from math import ceil, floor, sqrt
from itertools import permutations
from typing import List, Tuple


def factors(n) -> List[int]:
    factor_list = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factor_list.append(i)
            if i != n // i:
                factor_list.append(n // i)
    return factor_list

def max_abs_diff_in_subarray_sum(n, l):
    if n == 1:
        return 0
    
    pre = [0] * n
    pre[0] = l[0]
    for i in range(1, n):
        pre[i] = pre[i - 1] + l[i]
    
    facts = factors(n)
    max_diff = 0
    
    for factor in facts:
        p = factor
        mx = float("-inf")
        mn = float("inf")
        
        for i in range(0, n, p):
            if i == 0:
                current_sum = pre[p - 1]
            else:
                current_sum = pre[min(i + p - 1, n - 1)] - pre[i - 1]
            mx = max(mx, current_sum)
            mn = min(mn, current_sum)
        
        max_diff = max(max_diff, abs(mx - mn))
    
    return max_diff


t = 0
def main() -> None:
    
    n = int(input())
    l = list(map(int, input().split()))
    
    print(max_abs_diff_in_subarray_sum(n,l))

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
