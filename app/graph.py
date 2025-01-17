import networkx as nx
from pyvis.network import Network
import yaml
from pathlib import Path

def load_yaml_data(file_path):
    """Load project data from YAML file."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def create_graph_from_yaml(data):
    """Create a NetworkX graph from the YAML data structure."""
    G = nx.Graph()
    
    def add_nodes_recursive(parent_name, node_data, prefix=''):
        """Recursively add nodes and their relationships to the graph."""
        if isinstance(node_data, dict):
            # Add the parent node
            node_name = prefix + parent_name
            G.add_node(node_name, 
                      name=node_data.get('name', parent_name),
                      description=node_data.get('description', ''),
                      status=node_data.get('status', 'unknown'),
                      color=node_data.get('color', '#97c2fc'))  # Default pyvis blue
            
            # Process child nodes
            if 'nodes' in node_data:
                for node in node_data['nodes']:
                    child_name = node['name']
                    add_nodes_recursive(child_name, node, prefix=f"{node_name}_")
                    G.add_edge(node_name, f"{node_name}_{child_name}")
            
            # Process subnodes
            if 'subnodes' in node_data:
                for subnode in node_data['subnodes']:
                    child_name = subnode['name']
                    add_nodes_recursive(child_name, subnode, prefix=f"{node_name}_")
                    G.add_edge(node_name, f"{node_name}_{child_name}")
                    
            # Process next steps
            if 'next_steps' in node_data:
                for step in node_data['next_steps']:
                    child_name = step['name']
                    add_nodes_recursive(child_name, step, prefix=f"{node_name}_")
                    G.add_edge(node_name, f"{node_name}_{child_name}")

    # Start with the main projects
    for project_name, project_data in data['projects'].items():
        add_nodes_recursive(project_name, project_data)
    
    return G

def create_html_visualization(graph, output_path):
    """Create an HTML visualization of the graph using pyvis."""
    net = Network(height="750px", width="100%", bgcolor="#ffffff", font_color="black")
    
    # Add nodes with their attributes
    for node, attr in graph.nodes(data=True):
        net.add_node(node, 
                    label=attr.get('name', node),
                    title=attr.get('description', ''),
                    color=attr.get('color', '#97c2fc'))
    
    # Add edges
    for edge in graph.edges():
        net.add_edge(edge[0], edge[1])
    
    # Set physics layout options
    net.set_options("""
    {
      "physics": {
        "forceAtlas2Based": {
          "gravitationalConstant": -50,
          "centralGravity": 0.01,
          "springLength": 100,
          "springConstant": 0.08
        },
        "maxVelocity": 50,
        "solver": "forceAtlas2Based",
        "timestep": 0.35,
        "stabilization": {"iterations": 150}
      }
    }
    """)
    
    net.save_graph(str(output_path))