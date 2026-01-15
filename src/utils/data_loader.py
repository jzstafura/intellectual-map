“””
Data loading utilities for intellectual network visualization.
“””

import json
from pathlib import Path
from typing import Dict, Any

def load_problem_categories(data_dir: str = None) -> Dict[str, Any]:
“””
Load problem categories from JSON file.

```
Args:
    data_dir: Optional path to data directory. If None, uses default location.
    
Returns:
    Dictionary containing problem categories, connections, and bridge authors.
"""
if data_dir is None:
    data_dir = Path(__file__).parent.parent.parent / 'data' / 'processed'
else:
    data_dir = Path(data_dir)

filepath = data_dir / 'problem_categories.json'

if not filepath.exists():
    raise FileNotFoundError(f"Problem categories file not found: {filepath}")

with open(filepath, 'r') as f:
    return json.load(f)
```

def load_book_metadata(data_dir: str = None) -> Dict[str, Any]:
“””
Load book metadata from JSON file.

```
Args:
    data_dir: Optional path to data directory. If None, uses default location.
    
Returns:
    Dictionary containing reading statistics, patterns, and metadata.
"""
if data_dir is None:
    data_dir = Path(__file__).parent.parent.parent / 'data' / 'processed'
else:
    data_dir = Path(data_dir)

filepath = data_dir / 'book_metadata.json'

if not filepath.exists():
    raise FileNotFoundError(f"Book metadata file not found: {filepath}")

with open(filepath, 'r') as f:
    return json.load(f)
```

def validate_categories(categories: Dict[str, Any]) -> bool:
“””
Validate that categories dictionary has required structure.

```
Args:
    categories: Problem categories dictionary.
    
Returns:
    True if valid, raises ValueError otherwise.
"""
required_keys = ['metadata', 'problems', 'connections', 'key_bridge_authors']

for key in required_keys:
    if key not in categories:
        raise ValueError(f"Missing required key in categories: {key}")

# Validate problems have required fields
for problem, data in categories['problems'].items():
    required_problem_keys = ['description', 'estimated_books', 'avg_rating']
    for key in required_problem_keys:
        if key not in data:
            raise ValueError(f"Problem '{problem}' missing required field: {key}")

return True
```

def get_problem_list(categories: Dict[str, Any]) -> list:
“””
Extract list of problem names from categories.

```
Args:
    categories: Problem categories dictionary.
    
Returns:
    List of problem names.
"""
return list(categories['problems'].keys())
```

def get_bridge_authors(categories: Dict[str, Any]) -> list:
“””
Extract list of bridge author names from categories.

```
Args:
    categories: Problem categories dictionary.
    
Returns:
    List of bridge author names.
"""
return list(categories['key_bridge_authors'].keys())
```
