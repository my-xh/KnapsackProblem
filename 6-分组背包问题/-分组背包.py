"""
有 N 件物品和一个容量为 V 的背包。第 i 件物品的费用是 w[i]，价值是 v[i]。这些物品被划分为 k 组，每组中的物品互相冲突，最多选一件。
求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。

- 基本思路
dp[k][j] 表示前k组物品放入容量为j的背包获得的最大价值
dp[k][j] = Max(dp[k - 1][j], dp[k - 1][j - w[i]] + v[i]), 物品i∈组k

- 空间优化
dp[j] = Max(dp[j], dp[j - w[i]] + v[i]), j = V...w[i], 物品i∈组k
"""


# 基本动态规划
def method_1(V, group, w, v):
    dp = [0] * (V + 1)

    for k in group:
        for j in range(V, 0, -1):
            for i in group[k]:
                if j - w[i] >= 0:
                    dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    print(dp[V])
    print(dp)


if __name__ == '__main__':
    V = 10
    w = [2, 3, 4, 6, 2, 3]
    v = [1, 3, 8, 9, 8, 9]
    group = {
        1: [0, 1],
        2: [2, 3],
        3: [4, 5],
    }

    method_1(V, group, w, v)
