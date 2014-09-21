import fileinput

def count_zeros(s):
    return len(s) - len(s.lstrip('0'))

pow = dict()
for line in fileinput.input():
    words = line.split()
    pow[words[0]] = words[1]
    if words[0] == 'pow3:':
        one = count_zeros(pow['pow1:'])
        two = count_zeros(pow['pow2:'])
        three = count_zeros(pow['pow3:'])
        if one == three:
            if two > three:
                print 'two'
            else:
                print 'tie'
        elif one > three:
            if two > one:
                print 'two'
            else:
                print 'one'
        elif one < three:
            if two > three:
                print 'two'
            else:
                print 'three'
        else:
            print 'none'
    #print "WORD:", words[0], words[1]

