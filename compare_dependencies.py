import json

# Load dependencies from JSON files
with open('dependencies.json', 'r') as current_file:
    current_dependencies = json.load(current_file)

with open('dependencies_commit_12adaffe7.json', 'r') as commit_file:
    commit_dependencies = json.load(commit_file)

# Compare dependencies
added_dependencies = {}
removed_dependencies = {}

for file in current_dependencies:
    current_set = set(current_dependencies.get(file, []))
    commit_set = set(commit_dependencies.get(file, []))

    added = current_set - commit_set
    removed = commit_set - current_set

    if added:
        added_dependencies[file] = list(added)
    if removed:
        removed_dependencies[file] = list(removed)

# Save the results
with open('dependencies_added.json', 'w') as added_file:
    json.dump(added_dependencies, added_file, indent=4)

with open('dependencies_removed.json', 'w') as removed_file:
    json.dump(removed_dependencies, removed_file, indent=4)

print("Comparison complete! Results saved to 'dependencies_added.json' and 'dependencies_removed.json'")
