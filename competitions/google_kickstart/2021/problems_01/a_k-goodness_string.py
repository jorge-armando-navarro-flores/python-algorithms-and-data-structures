def goodness_score(s, n):
    score = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            score += 1
    return score
            
    

for t in range(int(input())):
    n, k = map(int, input().split(" "))
    s = list(input())
    operations = k - goodness_score(s, n)
    y = abs(operations)
    print(f"Case #{t+1}: {y}")

## SAMPLE INPUT ##

# 2
# 5 1
# ABCAA
# 4 2
# ABAA

