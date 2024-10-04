import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Function to visualize the array
def visualize(array, colorArray):
    plt.clf()  # Clear the figure
    plt.bar(range(len(array)), array, color=colorArray)
    plt.pause(0.1)  # Pause to allow visualization

# Bubble Sort Implementation
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            visualize(array, ['g' if x == j or x == j+1 else 'b' for x in range(len(array))])
        visualize(array, ['g' if x == len(array)-i-1 else 'b' for x in range(len(array))])

# Insertion Sort Implementation
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            visualize(array, ['g' if x == j or x == j+1 else 'b' for x in range(len(array))])
        array[j + 1] = key
        visualize(array, ['g' if x == i else 'b' for x in range(len(array))])

# Selection Sort Implementation
def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
            visualize(array, ['g' if x == j or x == min_idx else 'b' for x in range(len(array))])
        array[i], array[min_idx] = array[min_idx], array[i]
        visualize(array, ['g' if x == i else 'b' for x in range(len(array))])

if __name__ == "__main__":
    # Generate a random array
    array = random.sample(range(1, 101), 20)
    
    # Initialize matplotlib
    plt.ion()
    fig = plt.figure()
    
    # Choose the sorting algorithm
    sorting_algorithm = input("Choose sorting algorithm (bubble, insertion, selection): ").lower()
    
    if sorting_algorithm == "bubble":
        bubble_sort(array)
    elif sorting_algorithm == "insertion":
        insertion_sort(array)
    elif sorting_algorithm == "selection":
        selection_sort(array)
    else:
        print("Invalid sorting algorithm chosen.")
    
    plt.show(block=True)
