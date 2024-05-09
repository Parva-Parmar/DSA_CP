'''
https://codeforces.com/problemset/problem/1791/D
'''


import sys
from typing import List, Tuple
from queue import PriorityQueue as prq
from collections import deque as deq
from collections import defaultdict as dd
from collections import Counter as cnt
from bisect import bisect_left as bl
from bisect import bisect_right as br
from math import gcd, floor, sqrt, log, ceil, inf
from heapq import heapify, heappush, heappop, nlargest, nsmallest, heappushpop, heapreplace
# l.sort(key = lambda x: (-x[0], x[1]))
# l = sorted(l, key = lambda x: x[0], reverse = True)
def li(): return list(map(int, sys.stdin.readline().split()))
def mp(): return map(int, sys.stdin.readline().split())
def inp(): return int(sys.stdin.readline())
def st(): return str(sys.stdin.readline())
def strip(): return list(sys.stdin.readline().strip())
def pr(n): return sys.stdout.write(str(n)+"\n")
def prl(n): return sys.stdout.write(str(n)+" ")
def prlist(a): print("".join(a))
mod = 1000000007
maximum, minimum = float('inf'), float('-inf')
bi=lambda n: bin(n).replace("0b", "") 
yes=lambda : print("YES") ; no=lambda : print("NO")

import operator as op
from functools import reduce

class mydict:
    def __init__(self, func=lambda: 0):
        self.random = randint(0, 1 << 32)
        self.default = func
        self.dict = {}
    def __getitem__(self, key):
        mykey = self.random ^ key
        if mykey not in self.dict:
            self.dict[mykey] = self.default()
        return self.dict[mykey]
    def get(self, key, default):
        mykey = self.random ^ key
        if mykey not in self.dict:
            return default
        return self.dict[mykey]
    def __setitem__(self, key, item):
        mykey = self.random ^ key
        self.dict[mykey] = item
    def getkeys(self):
        return [self.random ^ i for i in self.dict]
    def __str__(self):
        return f'{[(self.random ^ i, self.dict[i]) for i in self.dict]}'

def ncr(n,r):
    r=min(r,n-r)
    numer=reduce(op.mul,range(n,n-r,-1),1)
    denom=reduce(op.mul,range(1,r+1),1)
    return numer//denom

def ncrmod(n,r,mod):
    p,q=1,1
    if n-r<r:
        r=n-r
    if r!=0:
        while r:
            p*=n
            k*=r
            m=gcd(p, k)
            p//=m
            k//=m
            n-=1
            r-=1
            p%=mod
    else:
        p=1
    return p
    
def fact(n):
	return math.factorial(n)
	
def perfect(n):
	return floor(sqrt(n))==ceil(sqrt(n))
	
def lcm(a,b):
    return a*b//gcd(a, b)

def dectobin(n):
    return bin(n).replace("0b", "")

def bintodec(n):
    return int(n,2)
	# can be used for converting number of any base to 10
    
def binarysearch(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return -1
    
def isprime(n):
	if (not n%2 and n!=2) or n<2:
	    return False
	i=3
	while i*i<=n:
	    if n%i==0:
	        return False
	    i+=2
	return True
	
def expo(a, n, M):
    ans=1
    while n>0:
        last_bit=n&1
        if(last_bit):
            ans=(ans*a)%M
        a=(a*a)%M
        n=n>>1
    return ans

def sequence(a):
    n=len(a)
    g,k,x=[a[0]],[1],0
    for i in range(1,n):
        if a[i]==a[i-1]:
            k[x]+=1
        else:
            g.append(a[i])
            k.append(1)
            x+=1
    return g,k

def checkgcd(a):
    if len(a)==1:
        return a[0]
    n=len(a)
    k=gcd(a[0],a[1])
    for i in range(2,n):
        k=gcd(k,a[i])
    return k
    
def prefix(a):
    p,s=[a[0]],a[0]
    for i in range(1,len(a)):
        s+=a[i]
        p.append(s)
    return p
    
def combo(n, n_list):
    if n<=0:
        yield []
        return
    for i in range(len(n_list)):
        c_num = n_list[i:i+1]
        for a_num in combo(n-1, n_list[i+1:]):
            yield c_num + a_num
            
    # res=combo(number of elements, list)
    # for i in res: u.append(i)
    # u contains all combinations in 2D list
    
def primefactors(n):
    ans=[]
    while not n%2:
        ans.append(2)
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while not n%i:
            ans.append(i)
            n//=i
    if n>2:
        ans.append(n)
    return ans
    
def ceiling(x):
    if x == int(x):
        return int(x)
    elif x > 0:
        return int(x) + 1
    else:
        return int(x)

def cal(x,y):
    if x>=y:
        return 0
    temp=y/xn
    val=log(temp,2)
    return ceiling(val)
    
def cnt(l:List[int]) -> int:
    c = 0
    
    for i in l:
        if(i>0):
            c+=1
    
    return c
        
def solve():
    n = inp()
    s = input()
    
    a = [0]*27
    b = [0]*27
    
    a[ord(s[0]) - 97] += 1
    
    for i in range(1,n):
        b[ord(s[i]) - 97] += 1
    
    mx = cnt(a)+cnt(b)
    
    for i in range(1,n-1):
        
        a[ord(s[i]) - 97] += 1
        b[ord(s[i]) - 97] -= 1
        # print(s[:i] , s[i:])
        # print(cnt(a), cnt(b))
        mx = max(mx, cnt(a)+cnt(b))
    
    print(mx)
    
    return
    
for loop in range(inp()):
	solve()
