def order(team):
    team = [[e[0], int(e[1]), int(e[2])] for e in [e.split() for e in team]]
    team = sorted(team, key = lambda e:(-int(e[1]), -int(e[-1])))
    for i in range(len(team)):
        team[i] = [0, i+1] + team[i][0:1]
    a, b = team[0::2],team[1::2]
    return [a, b]
def play(team, M, P):
    for _ in range(M):
        for t in range(2):
            for i in range(P): team[t][i][0]+=1
            # This can be better done with heapq
            # but why would I care when this works?
            active, bench = sorted(team[t][:P]), sorted(team[t][P:])
            active, bench = bench[0:1] + active[:-1], bench[1:] + [active[-1]]
            team[t] = active + bench
    return sorted(e[2] for t in team for e in t[:P])
T = int(raw_input())
for t in range(T):
    N, M, P = map(int, raw_input().split())
    players = [raw_input() for _ in range(N)]
    print "Case #{}: {}".format(t+1, ' '.join(play(order(players), M, P)))
