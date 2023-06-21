#Question 5: FirstKBinaryNumbers
#Given a number, k, return an array of the first k binary numbers, represented as strings.

def firstKBinaryNumbers(num):
    result = []
    queue = ['0','1']

    if num == 0:
        result.append(str(0))
        return result
    if num == 1:
         return queue
    while len(result) < num:
        number = queue.pop(0)
        result.append(number)
        if number != '0':
            queue.append(number + '0')
            queue.append(number + '1')

    return result

def main():
     print(firstKBinaryNumbers(5))
     print(firstKBinaryNumbers(10))
     print(firstKBinaryNumbers(0))
     print(firstKBinaryNumbers(1))


if __name__ == '__main__':
        main()
