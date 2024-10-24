import heapq
import numpy as np
import random

def greedy_best_first_tsp(distance_matrix, n, start=0):
    """
    Solves the Traveling Salesman Problem using the Greedy Best-First Search algorithm.
    This algorithm selects the nearest unvisited parish at each step.

    Parameters:
        distance_matrix (numpy.ndarray): A 2D array representing the distances between parishes.
        n (int): The number of parishes to visit.
        start (int): The index of the starting parish.

    Returns:
        tour (list): The order in which parishes are visited.
        total_distance (float): The total distance of the tour.
    """
    # Initialize a list to track visited parishes
    visited = [False] * n
    # List to store the order of the tour
    tour = [start]
    # Total distance traveled
    total_distance = 0
    # Current parish index
    current = start
    # Mark the starting parish as visited
    visited[current] = True

    # Continue until all parishes have been visited
    while len(tour) < n:
        # Priority queue to find the nearest unvisited parish
        pq = []
        for j in range(n):
            if not visited[j]:
                # Add each unvisited parish to the priority queue
                heapq.heappush(pq, (distance_matrix[current][j], j))

        # Get the nearest unvisited parish from the priority queue
        nearest_distance, nearest_parish = heapq.heappop(pq)
        # Add the nearest parish to the tour
        tour.append(nearest_parish)
        # Mark it as visited
        visited[nearest_parish] = True
        # Update the total distance
        total_distance += nearest_distance
        # Move to the newly visited parish
        current = nearest_parish

    # Add the distance to return to the starting parish to complete the tour
    total_distance += distance_matrix[current][start]
    # Add the starting parish to the end of the tour to complete the circuit
    tour.append(start)

    # Return the final tour and the total distance
    return tour, total_distance

def main():
    """
    Main function to run the TSP solution using user inputs.
    Allows the user to specify the starting parish and the number of parishes to visit.
    """
    # Distance matrix representing distances between the 12 parishes
    distance_matrix = np.array([
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

    # List of parish names for output formatting
    parish_names = [
        "Kingston", "St. Andrew", "St. Thomas", "Portland", "St. Mary",
        "St. Ann", "Trelawny", "St. James", "Hanover", "Westmoreland",
        "St. Elizabeth", "Manchester"
    ]
    total_parishes = len(parish_names)

    # Display the available parishes to the user
    print("Available parishes:")
    for i, parish in enumerate(parish_names):
        print(f"{i + 1}. {parish}")

    # Ask the user to choose the starting parish
    start_parish = int(input("Enter the number corresponding to the starting parish (1-12): ")) - 1
    # Validate the user's choice for the starting parish
    if start_parish < 0 or start_parish >= total_parishes:
        print("Invalid choice. Please enter a number between 1 and 12.")
        return

    # Ask the user to specify how many parishes to visit, including the starting parish
    num_parishes = int(input(f"Enter the number of parishes to visit (including the starting parish, 1-{total_parishes}): "))
    # Validate the number of parishes to visit
    if num_parishes < 1 or num_parishes > total_parishes:
        print(f"Invalid number. Please enter a number between 1 and {total_parishes}.")
        return

    # Randomly select the specified number of parishes, ensuring the starting parish is included
    selected_parishes = [start_parish]
    other_parishes = [i for i in range(total_parishes) if i != start_parish]
    selected_parishes += random.sample(other_parishes, num_parishes - 1)

    # Create a reduced distance matrix that only includes the selected parishes
    reduced_distance_matrix = distance_matrix[np.ix_(selected_parishes, selected_parishes)]
    # Update the number of selected parishes
    n = len(selected_parishes)

    # Perform the TSP using Greedy Best-First Search on the reduced matrix
    tour_indices, total_distance = greedy_best_first_tsp(reduced_distance_matrix, n, 0)

    # Map the tour indices back to the original parish names
    tour = [selected_parishes[i] for i in tour_indices]
    tour_names = [parish_names[i] for i in tour]

    # Output the tour and total distance
    print("\nThe tour is:", ' → '.join(tour_names))
    print("Total distance:", total_distance, "km")

if __name__ == "__main__":
    main()
