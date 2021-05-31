"""
如果将前面1、2、3中的三种背包问题混合起来。也就是说，有的物品只可以取一次（01 背包），有的物品可以取无限次（完全背包），有的物品可以取的次数有一个上限（多重背包）。应该怎么求解呢？

- 01背包与完全背包的混合
根据物品类别，状态转移方程选用倒序(01背包)或顺序(完全背包)的顺序求解

- 再增加多重背包
将多重背包问题转换成01背包问题
"""


# 基本动态规划
def method_1(V, w, v, p):
    n = len(w)
    dp = [0] * (V + 1)

    for i in range(n):
        if p[i] == 0:
            # 完全背包
            for j in range(w[i], V + 1):
                dp[j] = max(dp[j], dp[j - w[i]] + v[i])
        else:
            # 01背包或多重背包
            num, total = 1, p[i]
            while total > 0:
                group_w = w[i] * num
                group_v = v[i] * num
                for j in range(V, group_w - 1, -1):
                    dp[j] = max(dp[j], dp[j - group_w] + group_v)
                total = total - num if total >= num else 0
                num <<= 1

    print(dp[V])
    print(dp)


if __name__ == '__main__':
    V = 5
    w = [1, 2, 3, 4]
    v = [2, 4, 4, 5]
    p = [1, 1, 0, 2]

    method_1(V, w, v, p)
