import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    
    while K > heap[0]:
        try:
            heapq.heappush(heap, heapq.heappop(heap)+(heapq.heappop(heap)*2))
        except IndexError:
            return -1
        answer +=1        
    
    return answer
