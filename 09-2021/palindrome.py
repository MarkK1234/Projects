

def is_palindrome(teststr):
    if teststr == teststr[::-1]:
        return True
    return False

check = True
while check:
    teststr = input("Enter a string to test for a palindrome or 'exit':")

    if teststr == "exit":
        check = False
        break
    
    teststr = teststr.lower()

    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x



    print("Palindrome test:", is_palindrome(newstr))
    