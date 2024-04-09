import heapq
numbers=[2,4,6,8,10,1,5,7,12]
heapq.heapify(numbers)
print(numbers)

heapq.heappush(numbers,3)
print(numbers)

print(heapq.heappop(numbers))