"""
这种背包问题的物品间存在某种“依赖”的关系。也就是说，物品 i （附件）依赖于物品 j（主件），表示若选物品 i，则必须选物品 j。
为了简化起见，我们先设没有某个物品既依赖于别的物品，又被别的物品所依赖；另外，没有某件物品同时依赖多件物品。

- 基本思路
将主件和附件的所有可能组合看作一个物品组（一个也不选，只选主件，一个主件一个附件，一个主件两个附件...），只能从该物品组中挑选一个物品，w[k]和v[k]分别为第k组的主件费用和价值，
对附件集合进行一次01背包，找出费用为0...V-w[k]的最大价值g[0...V-w[k]], 将物品组简化为V-w[k]+1个物品，每个费用为u的物品的价值为g[u - w[k]] + v[k]， u∈[w[k], V]。

g[j] 表示第k组的附件i放入容量为j的背包获得的最大价值, w[k]为主件费用
g[j] = Max(g[j], g[j - w[i]] + v[i]), j = V-w[k]...w[i], 物品i∈第k组附件

dp[j] 表示前k组物品放入容量为j的背包获得的最大价值
dp[j] = Max(dp[j], dp[j - u] + g[u - w[k]] + v[k])， j = V...u, u = w[k]...V
"""


# 基本动态规划
def method_1(V, w, v, attach):
    n = len(w)
    dp = [0] * (V + 1)

    for k in range(n):
        # 先对当前组的附件进行01背包
        g = [0] * (V - w[k] + 1)
        for wi, vi in attach[k]:
            for j in range(V - w[k], wi - 1, -1):
                g[j] = max(g[j], g[j - wi] + vi)
        # 从当前组挑选物品
        for j in range(V, 0, -1):
            for u in range(w[k], V + 1):
                if j - u >= 0:
                    dp[j] = max(dp[j], dp[j - u] + g[u - w[k]] + v[k])

    print(dp[V])
    print(dp)


if __name__ == '__main__':
    V = 1000
    w = [800, 400, 500]     # 主件费用
    v = [1600, 1200, 1000]  # 主件价值
    attach = [
        [(400, 2000), (300, 1500)],  # 附件(费用, 价值)
        [],
        [],
    ]

    method_1(V, w, v, attach)
