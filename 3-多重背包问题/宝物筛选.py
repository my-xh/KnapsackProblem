"""
题目描述
终于，破解了千年的难题。小 FF 找到了王室的宝物室，里面堆满了无数价值连城的宝物。

这下小 FF 可发财了，嘎嘎。但是这里的宝物实在是太多了，小 FF 的采集车似乎装不下那么多宝物。看来小 FF 只能含泪舍弃其中的一部分宝物了。

小 FF 对洞穴里的宝物进行了整理，他发现每样宝物都有一件或者多件。他粗略估算了下每样宝物的价值，之后开始了宝物筛选工作：
小 FF 有一个最大载重为 W 的采集车，洞穴里总共有 n 种宝物，每种宝物的价值为 v_i，重量为 w_i，每种宝物有 m_i 件。
小 FF 希望在采集车不超载的前提下，选择一些宝物装进采集车，使得它们的价值和最大。

输入格式
第一行为一个整数 n 和 W，分别表示宝物种数和采集车的最大载重。

接下来 n 行每行三个整数 v_i,w_i,m_i。

输出格式
输出仅一个整数，表示在采集车不超载的情况下收集的宝物的最大价值。

输入输出样例
输入 #1
4 20
3 9 3
5 9 1
9 4 2
8 1 3

输出 #1
47
"""

print('输入：')
n, W = (int(i) for i in input().split())
v, w, m = [], [], []
for _ in range(n):
    i, j, k = (int(i) for i in input().split())
    v.append(i)
    w.append(j)
    m.append(k)

dp = [0] * (W + 1)
for i in range(n):
    num, total = 1, m[i]
    while total > 0:
        if num > total:
            num = total
        group_w = w[i] * num
        group_v = v[i] * num
        for j in range(W, group_w - 1, -1):
            dp[j] = max(dp[j], dp[j - group_w] + group_v)
        total -= num
        num <<= 1

print('\n输出:')
print(dp[W])
