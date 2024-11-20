import json

# Load the JSON file
with open('react/dependencies.json', 'r') as file:
    data = json.load(file)

# Calculate the number of dependencies for each file
dependencies_count = {file: len(dependencies) for file, dependencies in data.items()}

# Sort files by the number of dependencies in descending order
sorted_dependencies = sorted(dependencies_count.items(), key=lambda x: x[1], reverse=True)

# Get the top 3 files with the highest number of dependencies
top_files = sorted_dependencies[:3]

# Print the results
print("Top 3 files with the most dependencies:")
for file, count in top_files:
    print(f"{file}: {count} dependencies")

# Save the top 3 files to a new JSON file
top_files_dict = {file: data[file] for file, _ in top_files}

with open('top_dependencies.json', 'w') as output_file:
    json.dump(top_files_dict, output_file, indent=4)

print("Top dependencies saved to top_dependencies.json")
