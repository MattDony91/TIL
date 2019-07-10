def fibonacci(num):
    preNum, postNum = 1, 1
    fiboList = [preNum, postNum]
    if num == 1:
        print([1])
    elif num == 2:
        print([1, 1])
    else:
        while num - 2 > 0:
            fiboList.append(preNum + postNum)
            temp = postNum + preNum
            preNum = postNum
            postNum = temp
            num -= 1
        print(fiboList)

inputNum = int(input())
fibonacci(inputNum)