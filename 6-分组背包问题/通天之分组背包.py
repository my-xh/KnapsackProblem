"""
题目描述
自 01 背包问世之后，小 A 对此深感兴趣。一天，小 A 去远游，却发现他的背包不同于 01 背包，他的物品大致可分为 k 组，每组中的物品相互冲突，现在，他想知道最大的利用价值是多少。

输入格式
两个数 m,n，表示一共有 n 件物品，总重量为 m。

接下来 n 行，每行 3 个数 a_i,b_i,c_i，表示物品的重量，利用价值，所属组数。

输出格式
一个数，最大的利用价值。

输入输出样例
输入 #1
45 3
10 10 1
10 5 1
50 400 2
输出 #1
10
"""

from collections import defaultdict

print('输入:')
m, n = (int(i) for i in input().split())
a, b, c = [], [], defaultdict(list)
for idx in range(n):
    ai, bi, ci = (int(i) for i in input().split())
    a.append(ai)
    b.append(bi)
    c[ci].append(idx)

dp = [0] * (m + 1)
for k in c:
    for j in range(m, 0, -1):
        for i in c[k]:
            if j - a[i] >= 0:
                dp[j] = max(dp[j], dp[j - a[i]] + b[i])

print('输出:')
print(dp[m])
