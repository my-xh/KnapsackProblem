"""
问题描述
新学期快乐！
成为大三的小A意识到自己没有太多时间来解决问题，因为还有其他事情要做，这让她几乎要疯了。
更何况，她的上司告诉她，有几个任务，她必须至少选择一项工作来做，但有些事情对老板来说毫无意义，她最多只能选择一项去做。
而对于其他工作，她可以随心所欲。我们只是将她可以选择的东西定义为“工作”。工作需要时间，并给小A带来一些快乐（这意味着她总是愿意做这些工作）。
因此，您可以选择其中的最佳组合来给她带来最大的快乐点，也可以成为一个好的下属。 （这意味着她应该听从老板的建议）？
 
输入
有几个测试用例，每个测试用例以两个整数 n 和 T (0<=n,T<=100) 开头，n 组工作供您选择，T 分钟供她完成。以下是n组描述，每组描述以两个整数m和s开头（0<m<=100），
这个集合中有m个作业，集合类型为s，（0代表该集合至少要完成1项工作，1代表最多选择1项完成，2代表可以自由选择。）
然后跟随m对整数ci，gi（0 <= ci，gi <= 100），意味着完成第 i 个工作需要 ci 分钟，完成它可以获得 gi 点快乐。一项工作只能做一次。

输出
每个测试用例的一行包含我们可以从所有工作中选择的最大幸福点。如果她不能完成她老板想要的，就输出 -1 。

样本输入
3 3
2 1
2 5
3 8
2 0
1 0
2 1
3 2
4 3
2 1
1 1
3 4
2 1
2 5
3 8
2 0
1 1
2 8
3 2
4 4
2 1
1 1
1 1
1 0
2 1
5 3
2 0
1 0
2 1
2 0
2 2
1 1
2 0
3 2
2 1
2 1
1 5
2 8
3 2
3 8
4 9
5 10

样本输出
5
13
-1
-1
"""


print('输入:')
while True:
    try:
        n, T = (int(i) for i in input().split())
    except:
        break
    gp, tp = [], []
    for _ in range(n):
        m, s = (int(i) for i in input().split())
        tmp = []
        for _ in range(m):
            ci, gi = (int(i) for i in input().split())
            tmp.append((ci, gi))
        gp.append(tmp)
        tp.append(s)

    dp = [0] * (T + 1)
    for k in range(n):
        if tp[k] == 0:  # 至少完成一项工作
            g = [float('-inf')] * (T + 1)
            for ci, gi in gp[k]:
                for j in range(T, ci - 1, -1):
                    g[j] = max(g[j], g[j - ci] + gi, dp[j - ci] + gi)
            dp = g
        elif tp[k] == 1:    # 至多完成一项工作
            for j in range(T, 0, -1):
                for ci, gi in gp[k]:
                    if j - ci >= 0:
                        dp[j] = max(dp[j], dp[j - ci] + gi)
        elif tp[k] == 2:    # 可完成任意数量的工作
            for ci, gi in gp[k]:
                for j in range(T, ci - 1, -1):
                    dp[j] = max(dp[j], dp[j - ci] + gi)

    print('-' * 50)
    print(max(dp[T], -1))

print('-' * 50)
