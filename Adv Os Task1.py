class Block:
    def __init__(self, start, size, name=None):
        self.start = start
        self.size = size
        self.name = name

    def __repr__(self):
        status = self.name if self.name else "Free"
        return f"[{status}: {self.start} -> {self.start + self.size - 1} ({self.size} bytes)]"


class MemoryAllocator:
    def __init__(self, total_size):
        self.total_size = total_size
        self.memory = [Block(0, total_size)]

    def display_memory(self):
        for block in self.memory:
            print(block)
        print("-" * 40)

    def add_process(self, name, size):
        for i, block in enumerate(self.memory):
            if block.name is None and block.size >= size:
                new_block = Block(block.start, size, name)
                remaining_size = block.size - size
                if remaining_size > 0:
                    remaining_block = Block(block.start + size, remaining_size)
                    self.memory[i:i+1] = [new_block, remaining_block]
                else:
                    self.memory[i] = new_block
                print(f"Process '{name}' added successfully.")
                return
        print(f"Failed to add process '{name}': Not enough contiguous memory (External Fragmentation).")

    def remove_process(self, name):
        for i, block in enumerate(self.memory):
            if block.name == name:
                block.name = None
                print(f"Process '{name}' removed.")
                self.merge_free_blocks()
                return
        print(f"Process '{name}' not found.")

    def merge_free_blocks(self):
        i = 0
        while i < len(self.memory) - 1:
            if self.memory[i].name is None and self.memory[i+1].name is None:
                self.memory[i].size += self.memory[i+1].size
                del self.memory[i+1]
            else:
                i += 1

    def compact_memory(self):
        new_memory = []
        current_start = 0
        for block in self.memory:
            if block.name is not None:
                new_block = Block(current_start, block.size, block.name)
                new_memory.append(new_block)
                current_start += block.size

        remaining = self.total_size - current_start
        if remaining > 0:
            new_memory.append(Block(current_start, remaining))
        self.memory = new_memory
        print("Memory compacted.")


# ex
if __name__ == '__main__':
    mem = MemoryAllocator(1000)
    mem.display_memory()

    mem.add_process("A", 200)
    mem.add_process("B", 300)
    mem.add_process("C", 100)
    mem.display_memory()

    mem.remove_process("B")
    mem.display_memory()

    mem.add_process("D", 350)  #  EF
    mem.display_memory()

    mem.compact_memory()
    mem.display_memory()

    mem.add_process("D", 350)
    mem.display_memory()
