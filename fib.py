from __future__ import print_function
import argparse

SEQ = [1,1,1,3,5,9,17,31]

def foobar(num):
    if num < 3: 
        return 1 
    else:
        return foobar(num - 3) + foobar(num -2) + foobar(num -1 )

def fib_v2(target):
    a = b = c = 1
    for _ in range(target):
        yield a 
        a, b, c = b, c, a + b + c 

__fib_cache = {}
def fib(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib(n-2) + fib(n-1)
        return __fib_cache[n]

def nVal(i):
    v = [ 1, 1, 1 ]
    for num in range(2,i):
        t = sum(v)
        v.remove(min(v))
        v.append(t)
    return t

def dVal(i):
    v = deque([ 1, 1, 1 ])
    for num in range(2,i):
        t = sum(v)
        v.popleft()
        v.append(t)
    return t

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--generate',
                        action='store_true',
                        help='Generates sequence',
                        )
    parser.add_argument('-p', '--position', type=int,
                        help='Nth position of seq to get',
                        )
    args = parser.parse_args()
    GEN_SEQ = args.generate if args.generate else False
    N = args.position if args.position else 6
    if GEN_SEQ:
        for i in fib_v2(N):
            print(i)
    else:
        for i in fib_v2(N):
            continue
        print(i)
    """
    print(dVal(N))
    """
    """
    print(fib(N))
    """
