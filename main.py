import math
import numpy as np


def is_prime(n: int) -> bool:
    """Returns True if n is prime, using math.isqrt() for trial division limit."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check factors up to floor(sqrt(n)) using 6k +/- 1 optimization
    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def analyze_prime_density(start: int, stop: int, num_bins: int = 10):
    """Calculates and prints rolling prime density across numerical intervals."""
    if start < 0 or stop <= start or num_bins <= 0:
        raise ValueError("Invalid range or bin count provided.")

    # Generate sequence of numbers across the range
    numbers = np.arange(start, stop)

    # Vectorize the Python primality test over the NumPy array
    vectorized_is_prime = np.vectorize(is_prime)
    prime_mask = vectorized_is_prime(numbers)

    # Extract actual prime numbers found
    primes = numbers[prime_mask]

    # Calculate histogram counts and bin boundary edges
    counts, bin_edges = np.histogram(numbers, bins=num_bins, weights=prime_mask)

    total_numbers = stop - start
    total_primes = len(primes)
    overall_density = (total_primes / total_numbers) if total_numbers > 0 else 0.0

    print(f"\n--- Prime Density Analysis [{start} to {stop - 1}] ---")
    print(f"Total Numbers Evaluated : {total_numbers}")
    print(f"Total Primes Found      : {total_primes}")
    print(f"Overall Density         : {overall_density:.4%}\n")

    print(f"{'Interval Range':<25} | {'Primes':<8} | {'Bin Size':<10} | {'Density':<8}")
    print("-" * 60)

    for i in range(num_bins):
        low = bin_edges[i]
        high = bin_edges[i + 1]
        count = int(counts[i])
        bin_size = int(high - low)
        density = count / bin_size if bin_size > 0 else 0.0

        print(
            f"[{low:10.1f}, {high:10.1f}) | {count:<8} | {bin_size:<10} | {density:.4%}"
        )


if __name__ == "__main__":
    try:
        # Example run: evaluate range from 1 to 100,000 using 10 intervals
        analyze_prime_density(start=1, stop=100_000, num_bins=10)
    except Exception as e:
        print(f"An error occurred: {e}")