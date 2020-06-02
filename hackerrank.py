def buildPalindrome(a, b):
    substrings = lambda a:[a[i:j] for i in range(len(a)+1) for j in range(i+1, len(a)+1)]
    ispalindrome = lambda a:list(a[:len(a)//2])==list(reversed(a))[:len(a)//2]
    
    m = 0
    palindrome = '-1'
    for sa in substrings(a):
        for sb in substrings(b):
            s = sa+sb
            if ispalindrome(s):
                if len(s)>m:
                    m = len(s)
                    palindrome = s
                elif len(s)==m:
                    if s<palindrome:
                        palindrome = s
    return palindrome

if __name__=="__main__":
    print(buildPalindrome("salut tu est une ordure espece de chien ", "tu est inutile osef de ce que tu racontes"))
