import random
from seedNum import seedNum
from generateNumber import rangeNum


def numplate(x):
    seedInput = x
    options = []
    number = []
    number = rangeNum.genNum(0)
    # print(type(number))
    # print(number)
    for num in number:
        seed = seedNum.seed(num)
        #print('Seed number: ' + str(seed))
        if seed == seedInput:
            options.append(num)
    #print(options)
    with open('numbers.txt', 'w') as writer:
        for o in options:
            writer.write(str(o))
            writer.write('\n')
        writer.close()
    return options
#numplate()
