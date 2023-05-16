
def solution(A):
    n = len(A)
    count = [0] * (n + 1)  
    
    for num in A:
        if num < 1 or num > n: 
            return 0
        if count[num] == 1: 
            return 1
        count[num] = 1
    
    return 1
