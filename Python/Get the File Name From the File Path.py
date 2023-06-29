## Example 1: Using os module

import os

# file name with extension
file_name = os.path.basename('/root/file.ext')

# file name without extension
print(os.path.splitext(file_name)[0])

## Example 2: Using os module

import os

print(os.path.splitext(file_name))

## Example 3: Using Path module

from pathlib import Path

print(Path('/root/file.ext').stem)
