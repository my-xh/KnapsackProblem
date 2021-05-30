"""
有 N 种物品和一个容量为 V 的背包。第 i 种物品最多有 p[i] 件可用，每件耗费的空间是 w[i]，价值是 v[i]。求解将哪些物品装入背包可使这些物品的耗费的空间总和不超过背包容量，且价值总和最大。

- 基本思路
dp[i][j] 表示前i个物品放入容量为j的背包得到的最大价值
dp[i][j] = Max(dp[i - 1][j - k*w[i]] + k*v[i]), 0 ≤ k ≤ p[i], k*w[i] ≤ j ≤ V

- 转换成01背包
将第i种物品看成 p[i] 件物品

- 二进制拆分
将 p[i] 件物品拆分成 2^0...2^(k-1), p[i]-2^k+1 件共 (k+1) 组物品， p[i]-2^k+1 > 0
0...p[i] 的任意数字可以通过其中若干组物品的数量相加得到
"""


# 基本动态规划
def method_1(V, w, v, p):
    n = len(w)
    dp = [[0] * (V + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        x = i - 1  # 第i件物品的索引
        for j in range(V + 1):
            dp[i][j] = max(dp[i - 1][j - k * w[x]] + k * v[x]
                           for k in range(min(p[x], j // w[x]) + 1))
    print(dp[n][V])
    print(dp)


# 转换成01背包
def method_2(V, w, v, p):
    ww, vv = [], []
    for i in range(len(p)):
        for _ in range(p[i]):
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
def method_3(V, w, v, p):
    ww, vv = [], []
    for i in range(len(p)):
        num, total = 1, p[i]
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


# 二进制拆分（空间优化）
def method_4(V, w, v, p):
    n = len(w)
    dp = [0] * (V + 1)

    for i in range(n):
        num, total = 1, p[i]
        while total > 0:
            if num > total:
                num = total
            group_w = w[i] * num
            group_v = v[i] * num
            for j in range(V, group_w - 1, -1):
                dp[j] = max(dp[j], dp[j - group_w] + group_v)
            total -= num
            num <<= 1

    print(dp[V])
    print(dp)


if __name__ == '__main__':
    V = 15
    w = [3, 4, 5]
    v = [2, 3, 4]
    p = [4, 3, 2]

    method_1(V, w, v, p)
    method_2(V, w, v, p)
    method_3(V, w, v, p)
    method_4(V, w, v, p)
