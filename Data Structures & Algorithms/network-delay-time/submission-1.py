class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list) # initilaizes adjacency list
        

        for u,v,w in times:
            edges[u].append((v,w)) # populates adjacency list

        minHeap = [(0,k)] # minHeap is just a list of tuples
        visit = set() # to help check if each node is visited
        t = 0 # the result that will be outputed


        while minHeap: 
            w1, n1 = heapq.heappop(minHeap) # will auto pop off the smallest w1(first element); if tie will look at n1(second element)
            if n1 in visit: #if node seen continue
                continue
            visit.add(n1) #if node not seen add
            t = max(t, w1) #update result

            for n2, w2 in edges[n1]:
                if n2 not in visit: # only push to heap if not already visited
                    heapq.heappush(minHeap, (w2 + w1, n2))

        return t if len(visit) == n else -1








        