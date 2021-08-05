# 计算偶数和
count = 1
ans = 0
while count <= 100:
    if not count % 2:
        ans += count
    count += 1
print(ans)
