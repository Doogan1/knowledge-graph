from flask import render_template
from app import app
from app.graph import load_yaml_data, create_graph_from_yaml, create_html_visualization
from pathlib import Path

@app.route('/')
def index():
    # Load and process the graph data
    yaml_path = Path(app.root_path) / 'data' / 'projects.yaml'
    data = load_yaml_data(yaml_path)
    graph = create_graph_from_yaml(data)
    
    # Create the visualization in the static directory
    vis_path = Path(app.root_path) / 'static' / 'network.html'
    create_html_visualization(graph, vis_path)
    
    return render_template('index.html')