class seedNum:
    def seed(x):
        # number = int(input('Enter a number with 4 or less digits: '))
        # print(number)
        # number = 1234
        number = x
        total = 0
        temp = number

        rem = temp % 1000
        quo = int(temp / 1000)
        total = total + quo

        temp = rem
        rem = temp % 100
        quo = int(temp / 100)
        total = total + quo

        temp = rem
        rem = temp % 10
        quo = int(temp / 10)
        total = total + quo
        total = total + rem

        #print('Total: ' + str(total))

        num = total
        sum = 0
        if num / 10 != 0:
            temp = num
            quo = int(temp / 10)
            rem = temp % 10
            sum = sum + quo
            sum = sum + rem
        return sum
