Advanced OS Task 1 – Memory Allocator
This project simulates a basic contiguous memory allocation system using Python. It demonstrates key concepts such as adding and removing processes, memory fragmentation, and compaction.
Features
•	- Simulates contiguous memory allocation
•	- Handles external fragmentation
•	- Supports memory compaction
•	- Simple memory state display
•	- CLI-based interaction
File Structure
- Adv Os Task1.py – Main Python script containing:
•	  - Block class: represents a memory block
•	  - MemoryAllocator class: handles memory operations
•	  - Sample usage in the __main__ section
---------------------------------------------------
1. Make sure you have Python 3 installed.
2. Run the script using:
You will see the memory state evolve as processes are added, removed, and memory is compacted.
Code Overview
Class: Block
Represents a single block in memory.
- Attributes: start, size, name
- Free blocks have name = None
Class: MemoryAllocator
- add_process(name, size)
- remove_process(name)
- compact_memory()
- display_memory()
Example Output
[Free: 0 -> 999 (1000 bytes)]
----------------------------------------
Process 'A' added successfully.
...
Memory compacted.
...
Concepts Covered
•	- Memory management in operating systems
•	- External fragmentation
•	- Compaction and coalescing free memory
Tasks Demonstrated
•	- Allocating memory to processes
•	- Removing processes and managing free space
•	- Simulating failure due to fragmentation
•	- Compacting memory to free up space
