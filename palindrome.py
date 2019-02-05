def isPalindrome(N): 
    rev = reverse(N) 
    if (N == rev): 
        return True
    return False
  N = 1221
ans = isPalindrome(N) 
  if ans == 1: 
    print("Yes") 
else: 
    print("No") 
