# Knowledge Graph Project Manager

An interactive visualization tool for managing project relationships and documentation.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
knowledge-graph/
├── app/
│   ├── __init__.py    # Flask app initialization
│   ├── routes.py      # URL endpoints
│   ├── graph.py       # NetworkX/Pyvis logic
│   ├── data/          # YAML data files
│   ├── static/        # Static files
│   └── templates/     # HTML templates
└── docs/             # Additional documentation
```

## Adding Projects

Projects are defined in `app/data/projects.yaml`. Each project can have:
- name: Display name
- description: Project description
- status: Current status
- nodes: List of sub-projects or components
- subnodes: Additional nested components
- next_steps: Upcoming tasks or milestones

## Features

- Interactive network visualization
- Color-coded nodes based on status
- Expandable/collapsible node hierarchy
- Hover tooltips with project descriptions