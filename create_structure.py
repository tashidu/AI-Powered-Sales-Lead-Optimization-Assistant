import os

# Define the project structure
project_structure = {
    "ai_sales_assistant": {
        "backend": {
            "api": ["ads.py", "leads.py", "appointments.py", "transcripts.py", "scripts.py"],
            "models": ["lead.py", "appointment.py", "transcript.py", "script.py"],
            "services": ["ad_generator.py", "lead_generator.py", "appointment_agent.py", "transcript_analysis.py", "script_rewriter.py"],
            "main.py": None
        },
        "db": {
            "init.sql": None,
            "migrations": {}
        },
        "frontend": {
            "dashboard.py": None
        },
        "workflows": {
            "n8n_workflows.json": None
        },
        "requirements.txt": None
    }
}

def create_structure(base_path, structure):
    for key, value in structure.items():
        path = os.path.join(base_path, key)
        if value is None:
            # Create an empty file
            with open(path, "w") as f:
                f.write("")  # empty file
        elif isinstance(value, dict):
            # Create directory and recurse
            os.makedirs(path, exist_ok=True)
            create_structure(path, value)
        elif isinstance(value, list):
            # Create directory and files inside
            os.makedirs(path, exist_ok=True)
            for file_name in value:
                file_path = os.path.join(path, file_name)
                with open(file_path, "w") as f:
                    f.write("")  # empty file

# Create the project structure
create_structure(".", project_structure)

print("Project structure created successfully!")
