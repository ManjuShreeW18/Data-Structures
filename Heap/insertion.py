class Heap:
    def heapify(self, arr, i, size):
        parent = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Find largest among parent and children
        if left < size and arr[left] > arr[parent]:
            parent = left
        if right < size and arr[right] > arr[parent]:
            parent = right

        # If parent changed, swap and heapify subtree
        if parent != i:
            arr[i], arr[parent] = arr[parent], arr[i]
            self.heapify(arr, parent, size)

    def insert(self, arr, val):
        arr.append(val)          # Add new value at end
        size = len(arr)
        # Fix heap from last non-leaf node to root
        for i in range(size // 2 - 1, -1, -1):
            self.heapify(arr, i, size)

    def delete(self, arr, val):
        size = len(arr)
        for i in range(size):
            if arr[i] == val:          # Find value index
                arr[i], arr[size - 1] = arr[size - 1], arr[i]  # Swap with last
                arr.pop()               # Remove last element
                self.heapify(arr, i, len(arr))  # Fix heap at index i
                break

    def heapsort(self, arr):
        size = len(arr)
        # Build max heap
        for i in range(size // 2 - 1, -1, -1):
            self.heapify(arr, i, size)
        # Extract elements one by one
        for i in range(size - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # Move current max to end
            self.heapify(arr, 0, i)           # Heapify reduced heap


# Usage examples:

h = Heap()
arr = []

# Insert elements
h.insert(arr, 10)
h.insert(arr, 20)
h.insert(arr, 5)
print("Heap after insertions:", arr)

# Delete element 20
h.delete(arr, 20)
print("Heap after deleting 20:", arr)

# Insert more elements
h.insert(arr, 15)
h.insert(arr, 30)
print("Heap before sorting:", arr)

# Heap sort
h.heapsort(arr)
print("Sorted array:", arr)
