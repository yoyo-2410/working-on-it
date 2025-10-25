import heapq as hq

# (priority, job_name)
jobs = [(2, 'Job1'), (5, 'Job2'), (1, 'Job3')]
hq.heapify(jobs)

print("Initial Jobs (Min-Heap):", jobs)

while jobs:
    priority, job = hq.heappop(jobs)
    print(f"Processing {job} with priority {priority}")

    # Simulate an interrupt arriving dynamically
    if job == 'Job1':
        print("Interrupt! New high-priority job arrived (priority 0)")
        hq.heappush(jobs, (0, 'Urgent_Job'))

print("All jobs completed!")
