def fcfs(requests, head):
    total_movement = 0
    sequence = []
    current = head
    for req in requests:
        movement = abs(current - req)
        total_movement += movement
        sequence.append((current, req, movement))
        current = req
    return total_movement, sequence


def scan(requests, head, max_cylinders, direction='up'):
    total_movement = 0
    sequence = []
    requests = sorted(requests)
    current = head

    if direction == 'up':
        upper = [r for r in requests if r >= head]
        lower = [r for r in requests if r < head][::-1]
        run = upper + [max_cylinders - 1] + lower
    else:
        lower = [r for r in requests if r <= head][::-1]
        upper = [r for r in requests if r > head]
        run = lower + [0] + upper

    for req in run:
        movement = abs(current - req)
        total_movement += movement
        sequence.append((current, req, movement))
        current = req

    return total_movement, sequence


def cscan(requests, head, max_cylinders):
    total_movement = 0
    sequence = []
    requests = sorted(requests)
    current = head

    upper = [r for r in requests if r >= head]
    lower = [r for r in requests if r < head]

    run = upper + [max_cylinders - 1, 0] + lower

    for req in run:
        movement = abs(current - req)
        total_movement += movement
        sequence.append((current, req, movement))
        current = req

    return total_movement, sequence


def print_result(name, total, sequence):
    print(f"\n{name} Scheduling:")
    print("Order of execution and movements:")
    for cur, nxt, move in sequence:
        print(f"Head moves from {cur} to {nxt} => {move} cylinders")
    print(f"Total head movement: {total} cylinders")


def main():
    import random

    max_cylinders = int(input("Enter total number of cylinders: "))  # e.g., 5000
    queue_size = int(input("Enter size of the queue: "))             # e.g., 10
    initial_head = int(input("Enter initial head position: "))       # e.g., 143

    print("\nEnter the request queue (space separated):")
    queue_input = input().strip()
    if queue_input:
        requests = list(map(int, queue_input.split()))
        if len(requests) != queue_size:
            print("Mismatch in queue size and entered values.")
            return
    else:
        requests = [random.randint(0, max_cylinders - 1) for _ in range(queue_size)]
        print(f"Randomly generated queue: {requests}")

    total_fcfs, seq_fcfs = fcfs(requests, initial_head)
    total_scan, seq_scan = scan(requests, initial_head, max_cylinders)
    total_cscan, seq_cscan = cscan(requests, initial_head, max_cylinders)

    print_result("FCFS", total_fcfs, seq_fcfs)
    print_result("SCAN", total_scan, seq_scan)
    print_result("C-SCAN", total_cscan, seq_cscan)


if __name__ == "__main__":
    main()
