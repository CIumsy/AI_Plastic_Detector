import csv
import numpy as np

# Sample data for 7 runs and 10 images per run
# Replace these with actual data points extracted from the graphs

# Each array represents accuracy scores from 1 graph (7 graphs in total)
run_1 = [0.65, 0.32, 0.42, 0.32, 0.44, 0.43, 0.62, 0.42, 0.55, 0.53]
run_2 = [0.55, 0.60, 0.75, 0.54, 0.50, 0.44, 0.42, 0.42, 0.62, 0.61]
run_3 = [0.56, 0.50, 0.50, 0.39, 0.33, 0.58, 0.55, 0.43, 0.58, 0.40]
run_4 = [0.40, 0.51, 0.77, 0.53, 0.58, 0.40, 0.55, 0.40, 0.41, 0.48]
run_5 = [0.34, 0.45, 0.42, 0.63, 0.50, 0.65, 0.52, 0.54, 0.56, 0.51]
run_6 = [0.47, 0.48, 0.54, 0.40, 0.48, 0.48, 0.47, 0.48, 0.48, 0.48]
run_7 = [0.63, 0.40, 0.52, 0.38, 0.45, 0.40, 0.37, 0.48, 0.46, 0.47]

# List of all runs
all_runs = [run_1, run_2, run_3, run_4, run_5, run_6, run_7]

# Writing to a CSV file
csv_file = 'accuracy_scores.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Run/Image'] + [f'Image_{i+1}' for i in range(10)])  # 10 images
    # Write the data
    for i, run in enumerate(all_runs):
        writer.writerow([f'Run_{i+1}'] + run)

print(f"Accuracy data saved to {csv_file}")
