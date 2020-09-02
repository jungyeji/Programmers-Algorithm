import heapq

def solution(food_times, k):
    answer = 0
    heap = []
    length = len(food_times)
    
    for i in range(length):
        heap.append((food_times[i],i+1))
    
    heapq.heapify(heap)
    
    small = heap[0][0]
    prev= 0
    
    while k - ((small-prev)*length) >= 0:
        k -= (small-prev)*length
        length-=1
        prev, index = heapq.heappop(heap)
        if not heap:
            return -1
        small = heap[0][0]
    
    tmp = sorted(heap, key = lambda x:x[1])
    answer = tmp[k%len(heap)][1]
    return answer
