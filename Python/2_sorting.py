import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Bubble Sort with visualization
def bubble_sort_visual(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort")

    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    iteration = [0]
    
    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        ax.set_xlabel(f"Iteration: {iteration[0]}")

    anim = animation.FuncAnimation(fig, update_fig, frames=bubble_sort_generator(arr.copy()), fargs=(bar_rects, iteration), repeat=False)
    plt.show()

def bubble_sort_generator(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr.copy()

# Selection Sort with visualization
def selection_sort_visual(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    ax.set_title("Selection Sort")

    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    iteration = [0]
    
    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        ax.set_xlabel(f"Iteration: {iteration[0]}")

    anim = animation.FuncAnimation(fig, update_fig, frames=selection_sort_generator(arr.copy()), fargs=(bar_rects, iteration), repeat=False)
    plt.show()

def selection_sort_generator(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr.copy()

# Insertion Sort with visualization
def insertion_sort_visual(arr):
    fig, ax = plt.subplots()
    ax.set_title("Insertion Sort")

    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    iteration = [0]
    
    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        ax.set_xlabel(f"Iteration: {iteration[0]}")

    anim = animation.FuncAnimation(fig, update_fig, frames=insertion_sort_generator(arr.copy()), fargs=(bar_rects, iteration), repeat=False)
    plt.show()

def insertion_sort_generator(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr.copy()

# Merge Sort with visualization
def merge_sort_visual(arr):
    fig, ax = plt.subplots()
    ax.set_title("Merge Sort")

    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    iteration = [0]
    
    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        ax.set_xlabel(f"Iteration: {iteration[0]}")

    anim = animation.FuncAnimation(fig, update_fig, frames=merge_sort_generator(arr.copy()), fargs=(bar_rects, iteration), repeat=False)
    plt.show()

def merge_sort_generator(arr):
    if len(arr) <= 1:
        yield arr.copy()
        return

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    yield from merge_sort_generator(left_half)
    yield from merge_sort_generator(right_half)

    left_idx = 0
    right_idx = 0
    idx = 0

    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] < right_half[right_idx]:
            arr[idx] = left_half[left_idx]
            left_idx += 1
        else:
            arr[idx] = right_half[right_idx]
            right_idx += 1
        idx += 1
        yield arr.copy()

    while left_idx < len(left_half):
        arr[idx] = left_half[left_idx]
        left_idx += 1
        idx += 1
        yield arr.copy()

    while right_idx < len(right_half):
        arr[idx] = right_half[right_idx]
        right_idx += 1
        idx += 1
        yield arr.copy()


# Quick Sort with visualization
def quick_sort_visual(arr):
    fig, ax = plt.subplots()
    ax.set_title("Quick Sort")

    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    iteration = [0]
    
    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        ax.set_xlabel(f"Iteration: {iteration[0]}")

    def quick_sort(arr, low, high):
        if low < high:
            pivot_idx = partition(arr, low, high)
            yield arr.copy()
            yield from quick_sort(arr, low, pivot_idx)
            yield from quick_sort(arr, pivot_idx + 1, high)

    def partition(arr, low, high):
        pivot = arr[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    anim = animation.FuncAnimation(fig, update_fig, frames=quick_sort(arr, 0, len(arr) - 1), fargs=(bar_rects, iteration), repeat=False)
    plt.show()


# Generate a sample list
sample_list = random.sample(range(1, 101), 30)
print("Original list:", sample_list)

# Sort and visualize using Bubble Sort
bubble_sort_visual(sample_list.copy())

# Sort and visualize using Selection Sort
selection_sort_visual(sample_list.copy())

# Sort and visualize using Insertion Sort
insertion_sort_visual(sample_list.copy())

# Sort and visualize using Merge Sort
merge_sort_visual(sample_list.copy())

# Sort and visualize using Quick Sort
quick_sort_visual(sample_list.copy())
