from collections import defaultdict
def  tennison():    
    T = int(raw_input())
    for t in range(1, T+1):
        k, ps, pr, pi, pu, pw, pd, pl = map(float, raw_input().split())        
        k = int(k)
        F = [[defaultdict(int) for _ in range(k+1)] for _ in range(2)]
        F[0][0][pi] = 1.0
        for i in range(k):
            F[1] = [defaultdict(int) for _ in range(k+1)]
            for j in range(k):
                for pi, cumm_prob in F[0][j].iteritems():
                    # win
                    win = (pi*ps + (1-pi) * pr)
                    F[1][j][pi]      += cumm_prob * (1-pw) * win
                    F[1][j][min(1, pi + pu)] += cumm_prob * pw * win
                    # lose
                    loss = (pi * (1-ps) + (1-pi)*(1-pr))
                    F[0][j+1][pi]      += cumm_prob * (1-pl) * loss
                    F[0][j+1][max(0, pi - pd)] += cumm_prob * pl * loss
            # Swap current with the next
            F = F[::-1]
        ans = sum(sum(F[0][j].values()) for j in range(k))
        print "Case #{}: {:.6f}".format(t, ans)
tennison()


