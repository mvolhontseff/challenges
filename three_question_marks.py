from __future__ import print_function
import re

PATTERN = re.compile('\?')

TEST0 = "arrb6???4xxbl5???eee5" 
TEST1 = "acc?7??sss?3rr1??????5" 
TEST2 = "5??aaaaaaaaaaaaaaaaaaa?5?5"
TEST3 = "5??aaaaaaaaaaaaaaaaaaa?5???5"
TEST4 = "9???1???9???1???9"

TESTS = [TEST0, TEST1, TEST2, TEST3, TEST4]

ALL_TRUE = False

def foo(mystring):
    counter = 0
    first = ""
    for i in mystring:
        if i.isdigit():
            if not first:
                first = int(i) 
                continue
            if first:
                second = int(i)
                if first + second == 10 and counter == 3:
                    ALL_TRUE = True 
                    counter = 0
                elif first + second == 10 and counter != 3:
                    ALL_TRUE = False
                first = second 
                second = ""
                continue
        if PATTERN.match(i) and first:
            counter += 1
    return ALL_TRUE

for test in TESTS:
    print(foo(test))

"""
for i in TEST0:
    if re.search(PATTERN, i):
        print(i)
"""
