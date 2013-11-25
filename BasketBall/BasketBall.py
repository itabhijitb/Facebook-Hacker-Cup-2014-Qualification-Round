from operator import itemgetter
def order(team):
    team = [(e[0], int(e[1]), int(e[2])) for e in (e.split() for e in team)]
    # Players with a higher shot percentage are rated higher than players
    # with a lower shot percentage.
    # If two players have the same shot percentage, the taller player is rated
    # higher.
    team = sorted(team, key = itemgetter(1,2), reverse = True)
    # Subsequent process would not need height and shot percentage, so can be
    # dropped safely.
    # Re-create the team list as a tuple of
    #    1. Total Time Played (Initialized to 0)
    #    2. Draft Number
    #    3. Player Name
    team = [(0, i + 1) + t[0:1] for i, t in enumerate(team)] 
    #  Now the first team contains all the players with the odd draft numbers
    #  and the second team all the players with the even draft numbers.
    a, b = team[0::2],team[1::2]
    return [a, b]
def play(team, M, P):
    # Iterate for M minutes of play
    for _ in range(M):
        # Iterate over both the teams
        for t in range(2):
            # Current Players plays one game. Add to their mins count
            for i in range(P): team[t][i][0]+=1
            # If there are more than P players on a team after each minute of
            # the game the player with the highest total time played leaves the
            # playing field. Ties are broken by the player with the higher draft
            # number leaving first.
            #
            # This can be better done with heapq
            # but why would I care when this works?
            active, bench = sorted(team[t][:P]), sorted(team[t][P:])
            active, bench = bench[0:1] + active[:-1], bench[1:] + [active[-1]]
            team[t] = active + bench
    # The names should be printed in lexicographical order.
    return sorted(e[2] for t in team for e in t[:P])
T = int(raw_input())
for t in range(T):
    N, M, P = map(int, raw_input().split())
    players = [raw_input() for _ in range(N)]
    print "Case #{}: {}".format(t+1, ' '.join(play(order(players), M, P)))
