import math

def longest_side(a,b):
    """
    :param a: 输入参数a
    :param b: 输入参数b
    :return: 
    """
    return math.sqrt(a*a + b*b)

if __name__ == '__main__':
    print(longest_side.__doc__)
    print(longest_side(4,5))