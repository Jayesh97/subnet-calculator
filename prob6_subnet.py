import time
try:
    while(True):
        l = list()
        a = input('Enter a valid class B classful IP address : ')
        l = a.split('.')
        if (int(l[0]) > 127) &  (int(l[0]) < 192) & (int(l[1]) < 256) & (int(l[2]) == 0) & (int(l[3]) == 0):
            print('******You have entered a valid class B address*****')
            break
        else:
            print('\n********Invalid class B address********')
            print('Enter the range from 128.0.0.0 to 191.0.0.0')
    h = int(input('Now enter the number of hosts in a subnet : '))
    h = h+2
    for i in range(1,17):
        if(2**i/h > 1):
            s= i
            break
    #print(2**s)
    n = l.copy()
    if(2**s/256 >= 1):
        n[2] = int(int(n[2])+2**s/256)
    else:
        n[3] = int(int(n[3])+2**s)

    #print(n)

    if(2**s >= 256):
        n[3] = int(n[3])+255
        n[2] = int(n[2])-1
    else:
        n[3] = n[3] -1

    l[3] = int(l[3])
    str1 = '.'.join(str(e) for e in l)

    n[3] = int(n[3])
    str2 = '.'.join(str(e) for e in n)
    print('\nThe 1st available subnet range is (',str1,'-----',str2,')')
except:
    print('IP adress should have 4 octets')
time.sleep(100)