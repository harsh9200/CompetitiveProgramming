import os
import sys

import bisect
from itertools import accumulate
from collections import defaultdict


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        U = list(map(int, input().split()))
        S = list(map(int, input().split()))
        
        # ? Universities and their Students 
        # * 1 --> [6, 5, 5, 3]
        # * 2 --> [8, 1, 1]
        d = defaultdict(list)
        
        # ? Adding Students in Sorted Way
        for idx in range(N):
            d[U[idx]].append(S[idx])
        
        
        
        # ? Accumulating the List of Students
        # * 1 --> [6, 11, 16, 19]
        # * 2 --> [8, 9, 10]
        for idx in d:
            d[idx].sort(reverse=True)
            d[idx] = list(accumulate(d[idx]))
        
        Ans = [0] * N
        for k in range(1, N+1):
            need_to_delete = []
            
            for univ in d:
                if len(d[univ]) < k:
                    need_to_delete.append(univ)
                    continue
                Ans[k-1] += d[univ][len(d[univ]) // k * k-1]
            
            for univ in need_to_delete:
                del d[univ]
        print(*Ans)