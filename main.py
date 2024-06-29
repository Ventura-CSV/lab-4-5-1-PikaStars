import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers = []
    total = 0
    count = 0
    while (count < 5):
        count = count + 1
        num = random.randrange(0, 100)
        numbers.append(num)
    
    count = 0
    while (count < len(numbers)):
        total = total + numbers[count]
        count = count + 1
    
    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
