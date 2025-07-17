import os

folder_structure = {
    "Assets": {
        "3D_Models": ["Characters", "Environment", "Props", "Weapons"],
        "Animations": [],
        "Textures": [],
        "Audio": ["Music", "SFX", "Voice"],
        "UI": [],
        "Shaders": [],
        "VFX": []
    },
    "Code": {
        "Gameplay": [],
        "UI": [],
        "AI": [],
        "Tools": []
    },
    "Docs": {
        "Design": [],
        "Story": [],
        "References": []
    },
    "Builds": ["Windows", "Mac", "Linux"]
}

def create_structure(base_path, structure):
    for folder, content in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        if isinstance(content, dict):
            create_structure(folder_path, content)
        elif isinstance(content, list):
            for subfolder in content:
                os.makedirs(os.path.join(folder_path, subfolder), exist_ok=True)

if __name__ == "__main__":
    base_folder = os.getcwd()
    create_structure(base_folder, folder_structure)
    print(f"3D Video Game folder structure created in: {base_folder}")
