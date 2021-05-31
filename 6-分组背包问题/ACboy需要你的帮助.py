"""
问题描述
ACboy本学期有N门课，他计划最多花M天学习。当然，根据他在不同课程上花费的天数，他会从不同的课程中获得收益。N个课程的M天如何安排能让收益最大化？
 
输入
输入由多个数据集组成。数据集以一行包含两个正整数 N 和 M 开始，N 是课程数，M 是 ACboy 的天数。
接下来输入矩阵 A[i][j], (1<=i<=N<=100,1<=j<=M<=100).A[i][j] 表示 ACboy 花了 j 天在第 i 个课程上, 他将获得价值 A[i][j] 的利润。
N = 0 和 M = 0 结束输入。

输出
对于每个数据集，您的程序应该输出一行，其中包含 ACboy 将获得的最大利润的数量。

样本输入
2 2 
1 2 
1 3 
2 2 
2 1 
2 1 
2 3 
3 2 1 
3 2 1 
0 0

样本输出
3 
4 
6
"""

print('输入:')
while True:
    N, M = (int(i) for i in input().split())
    if N == 0 and M == 0:
        break
    group = []
    for _ in range(N):
        group.append([int(i) for i in input().split()])

    dp = [0] * (M + 1)
    for k in range(len(group)):
        for j in range(M, 0, -1):
            for i, v in enumerate(group[k]):
                w = i + 1
                if j - w >= 0:
                    dp[j] = max(dp[j], dp[j - w] + v)

    print('-' * 50)
    print(dp[M])

print('-' * 50)
