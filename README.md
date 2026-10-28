# Prime Density Profiler

> Empirical analysis of prime number distributions and rolling frequency densities across custom numeric intervals.

## Overview

Investigating the distribution of prime numbers over large integer ranges often presents performance bottlenecks due to redundant trial divisions and inefficient sequence storage. Manual script writing for number theory experiments frequently leads to memory bloat and slow execution times. **Prime Density Profiler** solves this operational friction by combining optimized trial division algorithms with vectorized NumPy operations. It provides developers and quantitative researchers with a structured, high-throughput utility to evaluate prime frequency shifts and binned statistical densities directly in Python.

## Under the Hood / How It Works

The engine operates through a multi-stage data processing pipeline:
1. **Wheel Factorization Primality Testing:** The core `is_prime` routine evaluates numbers below 2, handles small bases (2, 3), filters multiples of 2 and 3, and subsequently checks potential factors up to $\lfloor\sqrt{n}\rfloor$ using a $6k \pm 1$ stepping optimization. This bounds the search space and cuts redundant checks.
2. **Vectorized Sequence Generation:** Using `numpy.arange`, the utility generates contiguous integer arrays efficiently in memory without native Python list overhead.
3. **Array Vectorization & Masking:** Because scalar functions don't inherently process multi-element arrays, `numpy.vectorize` maps the primality predicate across the array to construct a boolean mask of prime indices.
4. **Statistical Binning:** `numpy.histogram` aggregates prime counts across user-defined interval bins using the boolean mask as weights, computing precise rolling densities for comparative analysis.

## Key Features

* **Optimized Trial Division:** Binds factor checks strictly to integer square roots using `math.isqrt()`.
* **Wheel Optimization:** Skips redundant modulo checks using the $6k \pm 1$ rule.
* **Vectorized Processing:** Leverages NumPy arrays to avoid slow Python `for` loops over large integer sets.
* **Granular Interval Histograms:** Calculates binned density distributions and percentage frequencies across customized ranges.

## Tech Stack & Core Dependencies Breakdown

* **Python 3.10+:** Utilized for type hint support and modern runtime performance.
* **`math` (Standard Library):** Supplies `math.isqrt()` for precise, integer-exact square root boundary calculations without floating-point inaccuracies.
* **`numpy` (v1.20+):** Core numerical library used for contiguous memory allocation (`numpy.arange`), vector mapping (`numpy.vectorize`), and weighted frequency aggregation (`numpy.histogram`).

## Environment & Web-Based Quick Start

### Running via GitHub Codespaces
1. Open the repository on GitHub and click the **Code** dropdown.
2. Select the **Codespaces** tab and click **Create codespace on main**.
3. Once the environment initializes, install dependencies and execute the script.

### Local Virtual Environment Setup
```bash
# Clone the repository
git clone [https://github.com/your-username/prime-density-profiler.git](https://github.com/your-username/prime-density-profiler.git)
cd prime-density-profiler

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install numpy

# Execute the analysis script
python main.py
```

## Repository Structure

```bash
prime-density-profiler/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── README.md
└── main.py
```

## Roadmap

**[ ] Type Stubs & Strict Typing:** Integrate mypy type annotations and comprehensive stub files to enforce strict static analysis across all numeric boundaries.

**[ ] Async / Multiprocessing Worker Pools:** Migrate large-scale range evaluations to concurrent process pools (concurrent.futures.ProcessPoolExecutor) to parallelize interval slicing.

**[ ] Structured JSON Export:** Add a CLI argument flag to export binned density metrics directly to structured JSON or CSV files for external visualization tools.
