"""
有N件物品和一个容量为V的背包。第i件物品的费用是w[i]，价值是v[i]，求将哪些物品装入背包可使价值总和最大。

- 基本思路
dp[i][j] 表示前i个物品放入容量为j的背包得到的最大价值
dp[i][j] = {
    dp[i - 1][j],                                  j = 0...w[i] - 1
    Max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i]), j = w[i]...V
}

- 空间优化
dp[j] = Max(dp[j], dp[j - w[i]] + v[i]), j = V...w[i]

- 常数优化
sum[i]为前i个物品的费用和
dp[j] = Max(dp[j], dp[j - w[i]] + v[i]), j = V...Max(w[i], V-sum[n]+sum[i])

- 初始化问题
恰好装满: dp[0][0] = 0, 其他为float('-inf')
不是必须装满: dp[0][j] = 0, j = 0...V
"""


# 基本动态规划
def method_1(V, w, v):
    n = len(w)
    dp = [[0] * (V + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        x = i - 1  # 第i件物品的索引
        for j in range(V + 1):
            if j - w[x] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1]
                               [j - w[x]] + v[x])
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[n][V])
    print(dp)


# 空间优化
def method_2(V, w, v):
    n = len(w)
    dp = [0] * (V + 1)

    for i in range(n):
        for j in range(V, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    print(dp[V])
    print(dp)


# 常数优化
def method_3(V, w, v):
    n = len(w)
    dp = [0] * (V + 1)

    _sum = [w[0]]
    for i in range(1, n):
        _sum.append(_sum[-1] + w[i])

    for i in range(n):
        bound = max(w[i], V - (_sum[n - 1] - _sum[i]))
        for j in range(V, bound - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    print(dp[V])
    print(dp)


if __name__ == '__main__':
    V = 20
    w = [2, 3, 4, 5, 9]
    v = [3, 4, 5, 8, 10]

    method_1(V, w, v)
    method_2(V, w, v)
    method_3(V, w, v)
