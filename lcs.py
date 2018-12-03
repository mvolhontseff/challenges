from __future__ import print_function
"""
'dogca'
'ogcat'

'dogc'
'ogca'
'gcat'

'dog'
'ogc'
'gca'
'cat'

'do'
'og'
'gc'
'ca'
'at'

example index increment/decrement strategy:
foobar
'abcdef'
foobar[0:len(foobar) -3]
'abc'
foobar[1:len(foobar) -2]
'bcd'
foobar[2:len(foobar) -1]
'cde'
foobar[3:len(foobar) -0]
'def'


"""
b = 'aaaaanhorsepumodqqqqqiqdogxop2vkmj32uqnhorsepumodqqqqqiqdogxop2vkmj32uqaaaaanhorsepumodqqqqqiqdogxop2vkmj32uqnhorsepumodqqqqqiqdogxop2vkmj32uq'
a = 'aaaaaaad78b9yyhorse3dogqqqqqbv2nssx9tlgwahorsepumodqqqqiqdo2vkmj32uq!aaaaanhorsepumodqqqqqiqdogxop2vkmj32uqnhorsepumodqqqqqiqdogxop2vkmj32uq%$&@&@&'

def lcs(a, b):
    if len(a) < len(b):
        shorter, longer = a, b  
    else:
        shorter, longer = b, a
    string_len = len(shorter)
    for i in range(string_len):
        for left, right in zip(range(i), range(i -1, -1, -1)): 
            result = shorter[left:string_len -right]
            if result in longer:
                return result 

print(lcs(a, b))
