from WordUtil import *
from WordHash import *
import heapq

class SearchState:
    def __init__(self, mapping, words_left):
        self.m = mapping
        self.l = words_left
    def candidates(self, position, thorough=False):
        return WordHash.hash_matches(self.l[position],thorough)
    def try_candidate(self, position, w):
        m2 = self.m.copy_and_extend(self.l[position], w)
        if not m2:
            return None
        return SearchState(m2, self.l[:position] + self.l[(position+1):])
    def __lt__(self, other):
        return False # hack to allow these to exist in priority queues

def solve(scrambled, cipher_guess = None):
    words = [WordUtil.strip(w) for w in scrambled.split(" ")]
    c = cipher_guess
    if not c:
        c = WordUtil.Cipher("", "")
    s = SearchState(c, words)
    q = [(0, s)]
    while q:
        (pri, p) = heapq.heappop(q)
        if len(p.l) < 1:
            print(p.m.apply(words))
        else:
            for w in p.candidates(0, False):
                pnext = p.try_candidate(0, w)
                if pnext:
                    heapq.heappush(q, (pri, pnext))
            for w in p.candidates(0, True):
                pnext = p.try_candidate(0, w)
                if pnext:
                    heapq.heappush(q, (pri+1, pnext))
    print("done")
