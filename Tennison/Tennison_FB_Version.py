def Tennison():
    def memoize(fn):
        memo = {}
        def helper(*args):
            if not args:
                memo.clear()
                return
            w, l, p = args
            key = (w, l, int(p*1000))
            if key not in memo:
                memo[key] = fn(w, l, p)
            return memo[key]
        return helper
    @memoize
    def calc(win, loss, prob):
        prob = min(1, max(0, prob))
        if win == k: return 1
        if loss == k: return 0
        return prob       * ps       * pw       * calc(win + 1, loss,     prob + pu) + \
               prob       * ps       * (1 - pw) * calc(win + 1, loss,     prob     ) + \
               prob       * (1 - ps) * pl       * calc(win,     loss + 1, prob - pd) + \
               prob       * (1 - ps) * (1 - pl) * calc(win,     loss + 1, prob     ) + \
               (1 - prob) * pr       * pw       * calc(win + 1, loss,     prob + pu) + \
               (1 - prob) * pr       * (1 - pw) * calc(win + 1, loss,     prob     ) + \
               (1 - prob) * (1 - pr) * pl       * calc(win,     loss + 1, prob - pd) + \
               (1 - prob) * (1 - pr) * (1 - pl) * calc(win,     loss + 1, prob     )
    T = int(raw_input())
    for t in range(1, T+1):
        k, ps, pr, pi, pu, pw, pd, pl = map(float, raw_input().split())        
        k = int(k)
        print "Case {}: {:.6f}".format(t, calc(0, 0, pi))
        #Initialize the memory
        calc()
Tennison()
