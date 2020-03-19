def solution(x, y):
    # Your code here
    # Sorry for bad coding, I just started Python :/,
    # but I'll get much better at it in no time ;).
    generations = 0
    xNum = int(x)
    yNum = int(y)
    if xNum > 0 and yNum > 0:
        if xNum == 1 and yNum == 1: return "0"
        if xNum == yNum: return "impossible"

        while xNum % yNum != 0 or yNum % xNum != 0:
            if yNum == 1: return str(xNum - 1)
            if xNum == 1: return str(yNum - 1)
            while xNum > (2 * yNum) or yNum > (2 * xNum):
                if yNum != 0 and xNum > (2 * yNum):
                    generations += (xNum / yNum)
                    xNum %= yNum
                if xNum != 0 and yNum > (2 * xNum):
                    generations += (yNum / xNum)
                    yNum %= xNum
                if xNum == 0 or yNum == 0:
                    return "impossible"
            while xNum > 1 or yNum > 1:
                if xNum > yNum:
                    xNum -= yNum
                    generations += 1
                elif yNum > xNum:
                    yNum -= xNum
                    generations += 1
                else:
                    return "impossible"
        return str(generations)
    return "impossible"