"""
题目描述
爱与愁大神后院里种了 n 棵樱花树，每棵都有美学值 C_i。爱与愁大神在每天上学前都会来赏花。爱与愁大神可是生物学霸，他懂得如何欣赏樱花：一种樱花树看一遍过，一种樱花树最多看 A_i 遍，
一种樱花树可以看无数遍。但是看每棵樱花树都有一定的时间 T_i。爱与愁大神离去上学的时间只剩下一小会儿了。求解看哪几棵樱花树能使美学值最高且爱与愁大神能准时（或提早）去上学。

输入格式
共 n+1行：

第 1 行：现在时间 T_s（几时：几分），去上学的时间 T_e（几时：几分），爱与愁大神院子里有几棵樱花树 n。这里的 T_s，T_e 格式为：hh:mm，其中 0 ≤ hh ≤ 23, 0 ≤ mm ≤ 59, 且 hh,mm,n 均为正整数。

第 2 行到第 n+1 行，每行三个正整数：看完第 i 棵树的耗费时间 T_i，第 i 棵树的美学值 C_i，看第 i 棵树的次数 P_i（P_i=0 表示无数次，P_i 是其他数字表示最多可看的次数 P_i）。

输出格式
只有一个整数，表示最大美学值。

输入输出样例
输入 #1
6:50 7:00 3
2 1 0
3 3 1
4 5 4
输出 #1
11

样例解释：赏第一棵樱花树一次，赏第三棵樱花树2次。
"""


def time_transform(t):
    h, m = (int(i) for i in t.split(':'))
    return h * 60 + m

print('输入:')
T_s, T_e, n = input().split()
T_s = time_transform(T_s)
T_e = time_transform(T_e)
n, T = int(n), T_e - T_s

t, c, p = [], [], []
for _ in range(n):
    i, j, k = (int(i) for i in input().split())
    t.append(i)
    c.append(j)
    p.append(k)

dp = [0] * (T + 1)
for i in range(n):
    if p[i] == 0:
        for j in range(t[i], T + 1):
            dp[j] = max(dp[j], dp[j - t[i]] + c[i])
    else:
        num, total = 1, p[i]
        while total > 0:
            group_t = t[i] * num
            group_c = c[i] * num
            for j in range(T, group_t - 1, -1):
                dp[j] = max(dp[j], dp[j - group_t] + group_c)
            total = total - num if total >= num else 0
            num <<= 1

print('输出:')
print(dp[T])
