import multiprocessing
import random
import time
import matplotlib.pyplot as plt

def sort_fragment(fragment):
    return sorted(fragment)

def parallel_sort(data,processes):
    if processes <=1:
        return sorted(data)

    n = len(data)
    chunk_size = n // processes
    chunks = [data[i*chunk_size : (i+1)*chunk_size] for i in range(processes-1)]
    chunks.append(data[(processes-1)*chunk_size:])

    with multiprocessing.Pool(processes=processes) as pool:
        sorted_parts = pool.map(sort_fragment, chunks)

    return sorted(sum(sorted_parts, []))


def run_tests():
    sizes = [10_000, 50_000, 100_000, 200_000]
    processes = [1, 2, 4]                        
    results = {}

    for p in processes:
        times = []
        for size in sizes:
            data = [random.randint(0, 1_000_000) for _ in range(size)]
            start = time.time()
            parallel_sort(data, p)
            end = time.time()
            times.append(end - start)
            print(f"Rozmiar: {size}, procesy: {p}, czas: {end - start:.4f}s")
        results[p] = times

    # --- rysowanie wykresu ---
    for p in processes:
        plt.plot(sizes, results[p], marker="o", label=f"{p} processes")

    plt.title("Time of sorting")
    plt.xlabel("Data size")
    plt.ylabel("Time [s]")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    run_tests()
