def isPalindrome(str, left, right):
    if left>=right:
        return "It is a Palindrome Word"
    if str[left] != str[right]:
        return "It is  NOT a Palindrome Word"
    else:
       return isPalindrome(str,left+1,right-1)

str="ABCKLCBA"
print(isPalindrome(str,0,(len(str)-1)))