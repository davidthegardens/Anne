import textdistance
import time

algo=textdistance.ratcliff_obershelp

print(algo("`12-'];,","`1903--]'"))

def testAlgo(algo):
    if algo('abb','bab')==algo('abb','abb'):
        print('not order dependent')
    else: print('order dependent')

    if algo('abbc','abcc')==algo('abbc','abbc'):
        print('not frequency dependent')
    else: print('frequency dependent')

    if algo('abcdedka','bsssowrbb')==algo('bsssowrbb','abcdedka'):
        print('commutative')
    else: print('non-commutative')

    st = time.process_time()
    algo("123whereamI4567890","1234567whereamI890")
    et = time.process_time()
    res = et - st
    print('CPU Execution time:', res*1000000)

    st = time.process_time()
    algo("123whereamI4567890123whereamI4567890","123whereamI45678901234567whereamI890")
    et = time.process_time()
    res2 = et - st
    print('Change in CPU Execution time for input size doubling:', (res2-res)*1000000)