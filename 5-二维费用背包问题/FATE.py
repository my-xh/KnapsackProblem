"""
问题描述
最近xhd正在玩一款叫做FATE的游戏，为了得到极品装备，xhd在不停的杀怪做任务。久而久之xhd开始对杀怪产生的厌恶感，但又不得不通过杀怪来升完这最后一级。
现在的问题是，xhd升掉最后一级还需n的经验值，xhd还留有m的忍耐度，每杀一个怪xhd会得到相应的经验，并减掉相应的忍耐度。当忍耐度降到0或者0以下时，xhd就不会玩这游戏。
xhd还说了他最多只杀s只怪。请问他能升掉这最后一级吗？

输入
输入数据有多组，对于每组数据第一行输入n，m，k，s(0 < n,m,k,s < 100)四个正整数。分别表示还需的经验值，保留的忍耐度，怪的种数和最多的杀怪数。
接下来输入k行数据。每行数据输入两个正整数a，b(0 < a,b < 20)；分别表示杀掉一只这种怪xhd会得到的经验值和会减掉的忍耐度。(每种怪都有无数个)
 
输出
输出升完这级还能保留的最大忍耐度，如果无法升完这级输出-1。
 
样本输入
10 10 1 10
1 1
10 10 1 9
1 1
9 10 2 10
1 1
2 2
 
样本输出
0
-1
1
"""


print('输入:')
while True:
    try:
        n, m, k, s = (int(i) for i in input().split())
    except:
        break
    a, b = [], []
    for _ in range(k):
        i, j = (int(i) for i in input().split())
        a.append(i)
        b.append(j)

    dp = [[0] * (m + 1) for _ in range(s + 1)]
    for i in range(k):
        for j in range(1, s + 1):
            for l in range(b[i], m + 1):
                dp[j][l] = max(dp[j][l], dp[j - 1][l - b[i]] + a[i])

    print('-' * 50)
    print(-1 if dp[s][m] < n else dp[s][m] - n)

print('-' * 50)
