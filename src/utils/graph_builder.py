“””
Graph building utilities for network visualization.
“””

import networkx as nx
from typing import Dict, Any

# Color palette for intellectual problems

PROBLEM_COLORS = {
‘Consciousness’: ‘#FF6B6B’,
‘Language’: ‘#4ECDC4’,
‘Violence’: ‘#FF8C42’,
‘Social Structure’: ‘#95E1D3’,
‘Aesthetic Experience’: ‘#F38181’,
‘Self/Subject’: ‘#AA96DA’,
‘Temporality’: ‘#FCBAD3’,
‘Place/Space’: ‘#A8D8EA’
}

def build_network_graph(categories: Dict[str, Any]) -> nx.Graph:
“””
Build NetworkX graph from problem categories data.

```
Args:
    categories: Dictionary containing problems, connections, and bridge authors.
    
Returns:
    NetworkX Graph object with problems and bridge authors as nodes.
"""
G = nx.Graph()

# Add problem nodes
for problem, data in categories['problems'].items():
    G.add_node(
        problem,
        node_type='problem',
        books=data['estimated_books'],
        avg_rating=data['avg_rating'],
        color=PROBLEM_COLORS.get(problem, '#CCCCCC'),
        description=data.get('description', '')
    )

# Add connections between problems
for connection in categories['connections']:
    G.add_edge(
        connection['from'],
        connection['to'],
        weight=connection['strength'],
        rationale=connection.get('rationale', '')
    )

# Add key bridge authors
for author, data in categories['key_bridge_authors'].items():
    G.add_node(
        author,
        node_type='work',
        size=data['significance'],
        color='#E0E0E0',
        primary_problem=data['primary_problem'],
        works=data.get('works', [])
    )
    
    # Connect to primary problem (stronger weight)
    G.add_edge(author, data['primary_problem'], weight=3)
    
    # Connect to bridged problems (weaker weight)
    for bridge in data['bridges']:
        G.add_edge(author, bridge, weight=1)

return G
```

def get_problem_nodes(G: nx.Graph) -> list:
“””
Get all nodes that are intellectual problems.

```
Args:
    G: NetworkX graph.
    
Returns:
    List of problem node names.
"""
return [node for node in G.nodes() if G.nodes[node].get('node_type') == 'problem']
```

def get_work_nodes(G: nx.Graph) -> list:
“””
Get all nodes that are works/authors.

```
Args:
    G: NetworkX graph.
    
Returns:
    List of work node names.
"""
return [node for node in G.nodes() if G.nodes[node].get('node_type') == 'work']
```

def get_node_stats(G: nx.Graph) -> Dict[str, Any]:
“””
Calculate basic statistics about the graph.

```
Args:
    G: NetworkX graph.
    
Returns:
    Dictionary with graph statistics.
"""
return {
    'total_nodes': G.number_of_nodes(),
    'problem_nodes': len(get_problem_nodes(G)),
    'work_nodes': len(get_work_nodes(G)),
    'total_edges': G.number_of_edges(),
    'avg_degree': sum(dict(G.degree()).values()) / G.number_of_nodes(),
    'density': nx.density(G)
}
```

def get_central_problems(G: nx.Graph, top_n: int = 3) -> list:
“””
Get most central problems by degree centrality.

```
Args:
    G: NetworkX graph.
    top_n: Number of top problems to return.
    
Returns:
    List of (problem, centrality) tuples.
"""
problem_nodes = get_problem_nodes(G)
centrality = nx.degree_centrality(G)

problem_centrality = [(node, centrality[node]) for node in problem_nodes]
problem_centrality.sort(key=lambda x: x[1], reverse=True)

return problem_centrality[:top_n]
```

def get_bridge_strength(G: nx.Graph, author: str) -> float:
“””
Calculate how strongly an author bridges problems.

```
Args:
    G: NetworkX graph.
    author: Name of the author node.
    
Returns:
    Bridge strength score (number of unique problem connections).
"""
if author not in G.nodes():
    raise ValueError(f"Author '{author}' not found in graph")

neighbors = list(G.neighbors(author))
problem_neighbors = [n for n in neighbors if G.nodes[n].get('node_type') == 'problem']

return len(problem_neighbors)
```
