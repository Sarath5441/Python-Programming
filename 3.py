ch=input()

if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A'
       or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print("Vowel")
elif(ch == '!' or ch == '@' or ch == '#' or ch == '$' or ch == '%' or ch == '^' or ch == '&' or ch == '*'
        or ch == '(' or ch == ')'):
    print("invalid")
else:
    print("Consonant")
