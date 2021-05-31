"""
对于每件物品，具有两种不同的费用 w[i] 和 g[i]，选择这件物品必须同时付出这两种费用，物品价值为 v[i]。对于每种费用都有一个可付出的最大值（背包容量）V 和 T。问怎样选择物品可以得到最大的价值。

- 基本思路
dp[i][j][k] 表示前i个物品付出j和k的费用时获取的最大价值
dp[i][j][k] = Max(dp[i - 1][j][k], dp[i - 1][j - w[i]][k - g[i]] + v[i])

- 空间优化
dp[j][k] = Max(dp[j][k], dp[j - w[i]][k - g[i]] + v[i]), j和k的遍历顺序由三种基本背包问题的类型来决定

- 物品总个数的限制
相当于每件物品多了一个件数的费用，每件物品的件数费用为1

- 复整数域的背包问题
一维背包问题是自然数域上的背包问题，二维背包问题相当于将数域扩大到了复整数域
"""


# 基本动态规划（01背包）
def method_1(V, T, w, g, v):
    n = len(w)
    dp = [[0] * (T + 1) for _ in range(V + 1)]

    for i in range(n):
        for j in range(V, w[i] - 1, -1):
            for k in range(T, g[i] - 1, -1):
                dp[j][k] = max(dp[j][k], dp[j - w[i]][k - g[i]] + v[i])

    print(dp[V][T])
    print(dp)


if __name__ == '__main__':
    V = 5
    T = 6
    w = [1, 2, 3, 4]
    g = [3, 4, 5, 6]
    v = [2, 4, 4, 5]

    method_1(V, T, w, g, v)
