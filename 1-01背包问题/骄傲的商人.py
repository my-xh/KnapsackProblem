"""
问题描述
最近，iSea去了一个古老的国家。这么长时间以来，它是世界上最富有和最强大的王国。结果，即使他们的国家不再那么富裕，这个国家的人民仍然感到非常自豪。
商家是最典型的商家，每个商家仅售出一件商品，价格为Pi，但如果您的钱少于Qi，他们就会拒绝与您进行交易，并且iSea评估每件商品的值为Vi。
如果他有M个货币单位，iSea可以得到的最大价值是多少？

 
输入
输入中有几个测试用例。

每个测试用例均以两个整数N，M（1≤N≤500、1≤M≤5000）开头，指示项目的编号和初始金额。
然后是N行，每行包含三个数字Pi，Qi和Vi（1≤Pi≤Qi≤100，1≤Vi≤1000），其含义在描述中。

输入在文件标记的结尾处终止。

输出
对于每个测试用例，输出一个整数，表示iSea可以获得最大值。

样本输入
2 10
10 15 10
5 10 5
3 10
5 10 5
3 5 6
2 7 3
2 10
5 9 2
1 7 3

样本输出
5
11

"""

while True:
    print('输入:')
    N, M = (int(i) for i in input().split())
    S = []
    for i in range(N):
        p, q, v = (int(i) for i in input().split())
        S.append((p, q, v))
    P, Q, V = zip(*sorted(S, key=lambda x: x[1] - x[0]))

    dp = [0] * (M + 1)
    for i in range(len(P)):
        for j in range(M, Q[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - P[i]] + V[i])

    print('输出:')
    print(dp[M])
    print(dp)
