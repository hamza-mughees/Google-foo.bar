def answer(n):
    pellets = int(n)
    operations = 0
  
    while pellets>1:
        if pellets%2==1: isEven = False
        else: isEven = True

        if isEven is False:
            toIncrement = True if (pellets-1)%4!=0 and pellets!=3 else False
            pellets = (pellets + 1) if toIncrement else (pellets - 1)
        else: pellets >>= 1

        operations += 1
  
    return operations