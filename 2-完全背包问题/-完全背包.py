"""
有N物品和一个容量为V的背包，每种物品都有无限件可用。第i种物品的费用是w[i]，价值是v[i]。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。

- 基本思路
dp[i][j] 表示第i个物品放入容量为j的背包得到的最大价值
dp[i][j] = Max(dp[i - 1][j - k*w[i]] + k*v[i]), 0 ≤ k*w[i] ≤ j ≤V

- 转换成01背包
将第i种物品看成 V/w[i] 件物品

- 二进制拆分
将第i种物品拆分成 2^0...2^k 件物品，其中 2^k * w[i] ≤ V

- 时间优化
dp[j] = Max(dp[i - 1][j], dp[i][j - w[i]] + v[i]), j = w[i]...V
"""


# 基本动态规划
def method_1(V, w, v):
    n = len(w)
    dp = [[0] * (V + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        x = i - 1  # 第i件物品的索引
        for j in range(V + 1):
            dp[i][j] = max(dp[i - 1][j - k * w[x]] + k * v[x]
                           for k in range(j // w[x] + 1))

    print(dp[n][V])
    print(dp)


# 转换成01背包
def method_2(V, w, v):
    ww, vv = [], []
    for i in range(len(w)):
        for _ in range(V // w[i]):
            ww.append(w[i])
            vv.append(v[i])

    n = len(ww)
    dp = [0] * (V + 1)

    for i in range(n):
        for j in range(V, ww[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - ww[i]] + vv[i])

    print(dp[V])
    print(dp)


# 二进制拆分
def method_3(V, w, v):
    ww, vv = [], []
    for i in range(len(w)):
        num, total = 1, V // w[i]
        while total > 0:
            if num > total:
                num = total
            ww.append(w[i] * num)
            vv.append(v[i] * num)
            total -= num
            num <<= 1

    n = len(ww)
    dp = [0] * (V + 1)

    for i in range(n):
        for j in range(V, ww[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - ww[i]] + vv[i])

    print(dp[V])
    print(dp)


# 时间优化
def method_4(V, w, v):
    n = len(w)
    dp = [0 for _ in range(V + 1)]

    for i in range(n):
        for j in range(w[i], V + 1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    print(dp[V])
    print(dp)


if __name__ == '__main__':
    V = 10
    w = [5, 7]
    v = [5, 8]

    method_1(V, w, v)
    method_2(V, w, v)
    method_3(V, w, v)
    method_4(V, w, v)
