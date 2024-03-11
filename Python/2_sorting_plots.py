import time
import random
import matplotlib.pyplot as plt

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

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

# Function to generate a random array
def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

# Function to measure time taken by each sorting algorithm
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Main function to compare sorting algorithms
def compare_sorting_algorithms(array_sizes):
    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    results = {alg: [] for alg in sorting_algorithms}

    for size in array_sizes:
        arr = generate_random_array(size)
        for alg_name, sort_func in sorting_algorithms.items():
            arr_copy = arr.copy()
            time_taken = measure_time(sort_func, arr_copy)
            results[alg_name].append(time_taken)

    return results

# Plotting function
def plot_results(results, array_sizes):
    for alg_name, times in results.items():
        plt.plot(array_sizes, times, label=alg_name)
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Sorting Algorithms')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    array_sizes = [100, 500, 1000, 2000, 5000]
    results = compare_sorting_algorithms(array_sizes)
    plot_results(results, array_sizes)
