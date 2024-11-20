**SE1_TASK1 contains：**
- All the detailed steps to complete task1, e.g. git commands, the use of the madge tool, use of python code 
- Screenshots of all the command and code execution.
- Screenshots of all important documents
- the meaning of the json file and md file in the directory.

**search_components.py**
- Search all the components in React v18.3.1 and generate components.json

**components.json**
- Contains all class-based components and functional components

**dependencies.json**
- Genrated by Madge, showing the dependencies of files in sourcecode of React v18.3.1

**find_top3_highdep_files.py**
- Find the top 3 files with the highest number of dependencies and document the info into top_dependencies.json

**top_dependencies.json**
- Contains the dependency information of the top 3 files with the highest number of dependencies

**commit_change.md**
- Document the commit hash that resulted in the most substantial changes between React v17.0.1 and v17.0.2, number of files changed, number of insertions and number of deletions.

**dependencies_commit_12adaffe7.json**
- Genrated by Madge, showing the dependencies of files in sourcecode of React v17.0.2(commit hash 12adaffe7 with the tag v17.0.2)

**compare_dependencies.py**
- Compare these dependencies in commit hash 12adaffe7 with the current ones(v18.3.1) and document the changes (dependencies introduced in dependencies_added.json and removed in dependencies_removed.json)

**dependencies_added.json**
- The new dependencies in v18.3.1 compared to v17.0.2

**dependencied_removed.json**
- The dependencies removed in v18.3.1 compared to v17.0.2


