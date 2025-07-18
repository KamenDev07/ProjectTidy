# Project File Organizer

A Python utility script to organize files in your working directory into categorized subfolders based on file types and optional filename suffixes. Ideal for projects involving 3D assets, textures, audio, code, and more.

---

## Features

- Automatically sorts files into predefined categories (e.g., 3D Models, Textures, Audio, Code).
- Extracts a suffix from filenames (e.g., `Character_Animation.fbx`) to create subfolders within categories.
- Prevents overwriting by moving files into structured folders.
- Prompts you for a project name and organizes files under the created proejct folder.

---

## Supported File Types

| Category     | Extensions                     |
|--------------|--------------------------------|
| 3D_Models    | `.fbx`, `.obj`, `.blend`, `.glb` |
| Textures     | `.png`, `.jpg`, `.jpeg`, `.tga`, `.bmp` |
| Audio        | `.mp3`, `.wav`, `.ogg`, `.flac` |
| Animations   | `.anim`, `.fbx` |
| Code         | `.cs`, `.cpp`, `.h`, `.py` |
| Shaders      | `.shader`, `.hlsl`, `.glsl` |
| Docs         | `.txt`, `.md`, `.pdf`, `.docx` |
| UI           | `.ui`, `.svg`, `.psd` |

---

## Usage

1. Place the script in the directory containing your files.
2. Run the script/
3. Enter your project name when prompted. This name will be used to create a root folder for the organized files.
4. The script will automatically move files into appropriate category folders and optional subfolders derived from filename suffixes.

---

## Example

For a file named:

```
Character_Animation.fbx
```

It will be organized into:

```
/YourProjectName/3DModels/Animation/Character_Animation.fbx
```
