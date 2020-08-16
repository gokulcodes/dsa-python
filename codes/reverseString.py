def reverseString(string):
    s1 = ''
    for i in string:
        s1 = i + s1
    return s1 

print(reverseString('simple'))