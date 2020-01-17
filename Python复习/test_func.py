def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input("enter string: ")
    if palindrome(s):
        print("Yay a palidrome")
    else:
        print('Not a palindrome')