from collections import Counter
while True:
    try:
        n = input()
        a = []
        e = []
        d = []
        t = 0
        resp = []
        for i in xrange(n):
            a.append(map(int, raw_input().split()))
            if a[i][0] == 1:
                t += 1
                e.append(a[i][1])
            else:
                d.append(i)
        eSort = sorted(e)
        inicio = 0
        for j in d:
            if a[j][1] == e[t - 1]:
                t -= 1
                resp.append("stack")
            if a[j][1] == e[inicio]:
                inicio += 1
                resp.append("queue")
            if a[j][1] == eSort[-1]:
                eSort.pop()
                resp.append("priority queue")
        mCommon = Counter(resp).most_common(2)
        if len(mCommon) == 0:
            print "impossible"
        elif len(mCommon) > 1 and mCommon[0][1] == mCommon[1][1]:
            print "not sure"
        else:
            print mCommon[0][0]
            print mCommon
    except:
        break
