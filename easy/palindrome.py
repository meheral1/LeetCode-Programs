def palindrome(x): 
    reverse = 0
    if x<0:
        y = abs(x)
    else:
        y = x

    while y>0:
        num = y % 10
        reverse = (reverse*10) + num
        y = y // 10
    
    if reverse == x:
        return True
    else:
        return False


x = int(input("enter any x: "))
print(f"Given x: {x} is a palindrome") if palindrome(x)==True else print(f"Given x: {x} is not a palindrome")

