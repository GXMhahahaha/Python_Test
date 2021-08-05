def fac(x):
    if x == 1:
        return 1
    return fac(x - 1) * x


ans = fac(3)
print(ans)

print("-----------------斐波那契动态规划------------------")
dp = [0] * 1000


def fib(n):
    if dp[n]:
        return dp[n]
    if n == 1 or n == 2:
        dp[n] = 1
        return dp[n]
    else:
        dp[n] = fib(n - 1) + fib(n - 2)
        return dp[n]


ans = fib(10)
print(ans)
for i in dp:
    if i:
        print(i)

dp = [10] * 100
print(dp)
