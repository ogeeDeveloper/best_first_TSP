import unittest
import numpy as np
from copy import deepcopy
from main import greedy_best_first_tsp
import matplotlib.pyplot as plt
import time

class TestTSPSolver(unittest.TestCase):
    def setUp(self):
        # [Previous setUp code remains exactly the same]
        # Basic 4x4 distance matrix for simple tests
        self.small_matrix = np.array([
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ])
        
        # Symmetric matrix where shortest neighbor path is obvious
        self.obvious_matrix = np.array([
            [0, 1, 100, 100],
            [1, 0, 1, 100],
            [100, 1, 0, 1],
            [100, 100, 1, 0]
        ])
        
        # Real distance matrix from the original code
        self.jamaica_matrix = np.array([
            [0, 10, 25, 60, 70, 80, 100, 130, 140, 160, 180, 150],
            [10, 0, 20, 55, 65, 75, 95, 125, 135, 155, 175, 145],
            [25, 20, 0, 45, 55, 70, 85, 110, 120, 140, 160, 130],
            [60, 55, 45, 0, 25, 40, 60, 80, 100, 120, 140, 110],
            [70, 65, 55, 25, 0, 30, 50, 75, 95, 115, 135, 105],
            [80, 75, 70, 40, 30, 0, 35, 55, 80, 100, 120, 90],
            [100, 95, 85, 60, 50, 35, 0, 30, 55, 75, 95, 65],
            [130, 125, 110, 80, 75, 55, 30, 0, 25, 50, 70, 40],
            [140, 135, 120, 100, 95, 80, 55, 25, 0, 30, 50, 30],
            [160, 155, 140, 120, 115, 100, 75, 50, 30, 0, 25, 55],
            [180, 175, 160, 140, 135, 120, 95, 70, 50, 25, 0, 40],
            [150, 145, 130, 110, 105, 90, 65, 40, 30, 55, 40, 0]
        ])

    # [All previous test methods remain exactly the same]
    def test_small_matrix_basic(self):
        """Test with a small 4x4 matrix starting from different positions"""
        tour, distance = greedy_best_first_tsp(self.small_matrix, 4, start=0)
        self.assertEqual(len(tour), 5)  # Should include return to start
        self.assertEqual(tour[0], tour[-1])  # Should return to start
        self.assertTrue(isinstance(distance, (int, float, np.integer, np.floating)))

    def test_obvious_path(self):
        """Test with a matrix where the greedy path follows lowest neighbors"""
        tour, distance = greedy_best_first_tsp(self.obvious_matrix, 4, start=0)
        self.assertEqual(tour[0], 0)  # Starts at 0
        self.assertEqual(tour[-1], 0)  # Returns to 0
        self.assertEqual(len(tour), 5)  # Complete tour length
        for i in range(len(tour) - 1):
            self.assertTrue(self.obvious_matrix[tour[i]][tour[i + 1]] in [1, 100])

    def test_different_starting_points(self):
        """Test that different starting points produce valid tours"""
        n = 4
        for start in range(n):
            tour, distance = greedy_best_first_tsp(self.small_matrix, n, start=start)
            self.assertEqual(len(tour), n + 1)
            self.assertEqual(tour[0], start)
            self.assertEqual(tour[-1], start)

    def test_jamaica_matrix_full(self):
        """Test the full Jamaica parish matrix"""
        n = 12
        tour, distance = greedy_best_first_tsp(self.jamaica_matrix, n, start=0)
        self.assertEqual(len(tour), n + 1)
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
        self.assertGreater(distance, 0)

    def test_jamaica_matrix_subset(self):
        """Test with a subset of parishes"""
        n = 6
        subset_indices = [0, 1, 2, 3, 4, 5]
        subset_matrix = self.jamaica_matrix[np.ix_(subset_indices, subset_indices)]
        tour, distance = greedy_best_first_tsp(subset_matrix, n, start=0)
        self.assertEqual(len(tour), n + 1)
        self.assertLess(distance, np.sum(self.jamaica_matrix))

    def test_matrix_modification(self):
        """Test that the function doesn't modify the input matrix"""
        original_matrix = deepcopy(self.small_matrix)
        greedy_best_first_tsp(self.small_matrix, 4, start=0)
        np.testing.assert_array_equal(self.small_matrix, original_matrix)

    def test_invalid_start_handling(self):
        """Test handling of invalid start indices"""
        with self.assertRaises(IndexError):
            greedy_best_first_tsp(self.small_matrix, 4, start=4)

    def test_zero_distance_handling(self):
        """Test handling of zero distances (same location)"""
        zero_matrix = np.zeros((4, 4))
        tour, distance = greedy_best_first_tsp(zero_matrix, 4, start=0)
        self.assertEqual(distance, 0)

    def test_path_continuity(self):
        """Test that the path is continuous (each point connects to the next)"""
        tour, distance = greedy_best_first_tsp(self.jamaica_matrix, 12, start=0)
        calculated_distance = 0
        for i in range(len(tour) - 1):
            calculated_distance += self.jamaica_matrix[tour[i]][tour[i + 1]]
        self.assertEqual(calculated_distance, distance)

def run_performance_analysis():
    """Run performance analysis after all tests complete"""
    print("\n=== Performance Analysis ===")
    
    # Test different matrix sizes
    sizes = [4, 6, 8, 10, 12]
    times = []
    distances = []
    
    for size in sizes:
        # Create random distance matrix
        matrix = np.random.randint(1, 100, size=(size, size))
        matrix = (matrix + matrix.T) // 2  # Make symmetric
        np.fill_diagonal(matrix, 0)
        
        # Measure execution time
        start_time = time.time()
        tour, distance = greedy_best_first_tsp(matrix, size, start=0)
        end_time = time.time()
        
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        times.append(execution_time)
        distances.append(distance)
        
        print(f"\nMatrix Size: {size}x{size}")
        print(f"Execution Time: {execution_time:.2f} ms")
        print(f"Tour Length: {len(tour)}")
        print(f"Total Distance: {distance}")
    
    # Create visualization
    plt.figure(figsize=(12, 5))
    
    # Plot 1: Execution Time vs Matrix Size
    plt.subplot(1, 2, 1)
    plt.plot(sizes, times, 'b-o', linewidth=2)
    plt.title('Execution Time vs Matrix Size')
    plt.xlabel('Matrix Size (n×n)')
    plt.ylabel('Execution Time (ms)')
    plt.grid(True)
    
    # Plot 2: Total Distance vs Matrix Size
    plt.subplot(1, 2, 2)
    plt.plot(sizes, distances, 'r-o', linewidth=2)
    plt.title('Total Distance vs Matrix Size')
    plt.xlabel('Matrix Size (n×n)')
    plt.ylabel('Total Distance')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print(f"Average Execution Time: {np.mean(times):.2f} ms")
    print(f"Maximum Execution Time: {np.max(times):.2f} ms")
    print(f"Average Distance: {np.mean(distances):.2f}")

if __name__ == '__main__':
    # Run all tests first
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    # Then run performance analysis
    run_performance_analysis()
