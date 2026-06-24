# File-Driven Data Processing Application
# Using External Modules

import csv
import statistics

# Function to read student data from file
def read_data(filename):
    marks = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            marks.append(int(row[2]))

    return marks

# Function to process data
def process_data(marks):
    total = sum(marks)
    average = statistics.mean(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, average, highest, lowest

# Main Program
filename = "students.csv"

try:
    marks = read_data(filename)

    total, average, highest, lowest = process_data(marks)

    print("----- Student Marks Report -----")
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Highest Mark:", highest)
    print("Lowest Mark:", lowest)

except FileNotFoundError:
    print("File not found!")
