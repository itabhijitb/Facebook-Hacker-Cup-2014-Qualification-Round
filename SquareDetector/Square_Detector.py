def square_detector():
    from itertools import chain, izip, dropwhile, takewhile
    T = int(raw_input())
    print T
    mat, line = None, None
    for t in range(1,T+1):
        try:
            N = int(raw_input())
            mat = list(raw_input() for _ in range(N))
            mat_it = iter(mat)
            mat = [next(dropwhile(lambda e: '#' not in e, mat_it))]
            mat += list(takewhile(lambda e: '#' in e, mat_it))
            for line in mat_it:
                if '#' in line:  raise StopIteration
            mat_it = izip(*mat)
            mat = [next(dropwhile(lambda e: '#' not in e, mat_it))]
            mat += list(takewhile(lambda e: '#' in e, mat_it))
            for line in mat_it:
                if '#' in line:  raise StopIteration
            if len(mat) != len(zip(*mat)) or '.' in list(chain(*mat)):
                raise StopIteration
            print "Case #{}: YES".format(t)
        except StopIteration:
            print "Case #{}: NO".format(t)
square_detector()
