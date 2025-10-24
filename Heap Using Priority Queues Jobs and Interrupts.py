import heapq as hq

# Jobs & interrupts (concept demonstration)
jobs = [(2,'job1'),(5,'job2'),(1,'job3')]
hq.heapify(jobs)

print("Initial Heap:", jobs)

while jobs:
    print("Processing:", hq.heappop(jobs))

print("All jobs completed!")
