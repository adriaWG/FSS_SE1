import os
import re
import json

def list_components_in_react_codebase(directory):
    # Define regex patterns for components
    class_based_pattern = r'class\s+(\w+)\s+extends\s+React\.(Component|PureComponent)'
    function_based_pattern = r'return\s+<.*?>'

    # Initialize results
    components = {
        "class_components": [],
        "function_components": []
    }

    # Walk through all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Match class-based components
                    class_matches = re.findall(class_based_pattern, content)
                    for match in class_matches:
                        components["class_components"].append({
                            "component": match[0],
                            "file": file_path
                        })
                    
                    # Match function-based components
                    if re.search(function_based_pattern, content):
                        components["function_components"].append({
                            "file": file_path
                        })
    
    # Return components found
    return components

# Define the directory to scan
react_codebase_directory = "react"

# List components
components_found = list_components_in_react_codebase(react_codebase_directory)

# Save results to a JSON file
output_file = "components.json"
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(components_found, json_file, indent=4)

print(f"Components listed successfully! Results saved in {output_file}")
