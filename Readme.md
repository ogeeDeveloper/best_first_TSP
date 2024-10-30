# Traveling Salesman Problem (TSP) Implementation

This repository contains a Python implementation of the Traveling Salesman Problem using a Greedy Best-First Search algorithm. The implementation is specifically designed to solve routing problems, with an example application for navigating Jamaican parishes. This is for the Analysis of Algorithm Assignment 2.

## Overview

The Traveling Salesman Problem (TSP) is a classic algorithmic problem where the goal is to find the shortest possible route that visits each location exactly once and returns to the starting point. This implementation uses a greedy best-first search approach to find a solution.

## Project Structure

```
BEST_FIRST_TSP/
├── main.py          # Core TSP implementation
├── test.py          # Test suite and performance analysis
└── Readme.md        # This file
```
## Requirements

### Python Version

- Python 3.12.7 or higher

### Required Libraries

```
numpy
matplotlib
```

To install the required libraries, run:
``` bash
pip install numpy matplotlib
```

## Installation

1. Clone or download this repository to your local machine
2. Navigate to the project directory
3. Install the required dependencies

``` bash
git clone https://github.com/ogeeDeveloper/best_first_TSP.git
cd BEST_FIRST_TSP
pip install -r requirements.txt
```

## File Descriptions

### main.py

Contains the core implementation of the TSP algorithm including:

- `greedy_best_first_tsp()`: Main function implementing the algorithm
- Distance matrix definitions
- Helper functions for route calculation
### test.py

Contains:
- Comprehensive test suite
- Performance analysis tools
- Visualization functions
## Usage

### Running the Main Program
``` bash
python main.py
```

This will:
1. Load the predefined distance matrix
2. Prompt for a starting parish (1-12)
3. Ask for the number of parishes to visit
4. Calculate and display the optimal route
### Running Tests and Performance Analysis
``` bash
python test.py
```

This will:
1. Run all test cases
2. Perform performance analysis
3. Display visualization graphs
4. Show performance metrics
## Test Cases

The test suite includes:
1. Basic functionality tests with small matrices
2. Tests with obvious optimal paths
3. Different starting point tests
4. Full Jamaica parish matrix tests
5. Subset matrix tests
6. Edge case handling tests
7. Performance analysis

## Performance Analysis

The performance analysis includes:
- Execution time measurements for different matrix sizes
- Distance calculations
- Visualization graphs showing:
    - Execution time vs matrix size
    - Total distance vs matrix size
- Summary statistics

## Example Output

When running the main program:
```
Available parishes:
1. Kingston
2. St. Andrew
3. St. Thomas
...

Enter the number corresponding to the starting parish (1-12): 1
Enter the number of parishes to visit (including the starting parish, 1-12): 5

The tour is: Kingston → St. Andrew → St. Thomas → Portland → St. Mary → Kingston
Total distance: 185 km
```

## Limitations

1. Being a greedy algorithm:
    - Does not guarantee the optimal solution
    - Performance depends on starting point
    - May miss globally optimal paths
    
1. Matrix constraints:
    - Requires symmetric distance matrix
    - All distances must be non-negative
    - Diagonal elements should be zero