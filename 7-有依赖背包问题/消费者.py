"""
问题描述
FJ 要去买东西，在那之前，他需要一些箱子来装他要买的各种东西。每个盒子都被分配了一些特定种类的东西（也就是说，如果他要购买其中一种东西，他必须事先购买盒子）。
每一种东西都有它自己的价值。现在FJ只有W美元可以购物，他打算用这笔钱获得最高的价值。
 
输入
第一行将包含两个整数，n（盒子的数量 1 <= n <= 50），w（FJ 拥有的金额，1 <= w <= 100000）然后是 n 行。
每行包含以下数字pi（第i个盒子的价格1<=pi<=1000）、mi（1<=mi<=10第i个盒子可以携带的商品数量）和mi对数字，价格cj (1<=cj<=100)，值vj(1<=vj<=1000000)
 
输出
对于每个测试用例，输出 FJ 可以得到的最大值

样本输入
3 800
300 2 30 50 25 80
600 1 50 130
400 3 40 70 30 40 35 60

样本输出
210
"""

print('输入:')
n, w = (int(i) for i in input().split())
p, c, v = [], [], []
for _ in range(n):
    pi, mi, *cv = input().split()
    p.append(int(pi))
    gpc, gpv = [], []
    for idx in range(0, int(mi) * 2, 2):
        cj, vj = cv[idx: idx + 2]
        gpc.append(int(cj))
        gpv.append(int(vj))
    c.append(gpc)
    v.append(gpv)

dp = [0] * (w + 1)
for k in range(n):
    g = [0] * (w - p[k] + 1)
    for cj, vj in zip(c[k], v[k]):
        for j in range(w - p[k], cj - 1, -1):
            g[j] = max(g[j], g[j - cj] + vj)
    for j in range(w, 0, -1):
        for u in range(p[k], w + 1):
            if j - u >= 0:
                dp[j] = max(dp[j], dp[j - u] + g[u - p[k]])

print('输出:')
print(dp[w])
