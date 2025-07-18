import os
import shutil

# Map file extensions to their primary categories
FILE_TYPE_MAP = {
    '3D_Models': ['.fbx', '.obj', '.blend', '.glb'],
    'Textures': ['.png', '.jpg', '.jpeg', '.tga', '.bmp'],
    'Audio': ['.mp3', '.wav', '.ogg', '.flac'],
    'Animations': ['.anim', '.fbx'],
    'Code': ['.cs', '.cpp', '.h', '.py'],
    'Shaders': ['.shader', '.hlsl', '.glsl'],
    'Docs': ['.txt', '.md', '.pdf', '.docx'],
    'UI': ['.ui', '.svg', '.psd'],
}

def create_folder(path):
    """Ensure the folder exists."""
    os.makedirs(path, exist_ok=True)

def detect_category(file_ext):
    """
    Determine the file category based on its extension.
    Returns the category name or None if unknown.
    """
    for category, extensions in FILE_TYPE_MAP.items():
        if file_ext in extensions:
            return category
    return None

def extract_suffix(filename):
    """
    Extract the suffix from the filename after the last underscore.
    For example, 'Character_Animation.fbx' -> 'Animation'
    """
    name_part = os.path.splitext(filename)[0]
    if '_' in name_part:
        return name_part.split('_')[-1].capitalize()
    return None

def move_files(base_path):
    """
    Process each file in the current directory:
    - Detect the file category based on extension.
    - Extract suffix for subfolder creation.
    - Move the file into the appropriate category/subfolder.
    """
    for item in os.listdir('.'):
        # Skip directories and this script itself
        if not os.path.isfile(item) or item == os.path.basename(__file__):
            continue

        # Get the file extension in lowercase
        ext = os.path.splitext(item)[1].lower()
        category = detect_category(ext)

        if category:
            # Create the category folder
            category_path = os.path.join(base_path, category)
            create_folder(category_path)

            # Extract potential subfolder name from filename suffix
            subfolder = extract_suffix(item)
            target_path = os.path.join(category_path, subfolder) if subfolder else category_path
            create_folder(target_path)

            # Move the file
            shutil.move(item, os.path.join(target_path, item))
            print(f"Moved {item} to {target_path}")
        else:
            print(f"No category for {item}, skipped.")

if __name__ == '__main__':
    # Prompt user for project name
    project_name = input("Enter project name: ").strip()
    if not project_name:
        print("Project name is required.")
        exit(1)

    # Create the main project folder
    project_path = os.path.join(os.getcwd(), project_name)
    create_folder(project_path)

    # Start processing and moving files
    move_files(project_path)

    print(f"Project setup complete at {project_path}")
