class rangeNum:
    def genNum(self):
        start = 1000
        end = 9999
        fourdigits = []

        while start <= end:
            start = start + 1
            fourdigits.append(start)
        return fourdigits
