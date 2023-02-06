import heapq

heap = []

heapq.heappush(heap, 20)
heapq.heappush(heap, 70)
heapq.heappush(heap, 10)
heapq.heappush(heap, 35)
heapq.heappush(heap, 50)

maximum = heapq.heappop(heap)
print(maximum)
