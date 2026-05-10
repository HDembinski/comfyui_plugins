# ComfyUI Plugins

Starter infrastructure for developing custom ComfyUI nodes in this repository.

## What is included

- ComfyUI plugin entrypoint in `__init__.py`
- Node modules under `nodes/`
- Native image sizes node in `nodes/native_image_sizes.py`
- Python project metadata in `pyproject.toml`
- Development dependency file in `requirements-dev.txt`
- VS Code Python + Ruff defaults in `.vscode/`
- Windows helper script to link this repo into ComfyUI: `scripts/link_to_comfyui.ps1`

## Quick start

1. Create and activate a Python virtual environment.
2. Install development dependencies:

	```powershell
	pip install -r requirements-dev.txt
	```

3. Link this repo into your local ComfyUI installation:

	```powershell
	.\scripts\link_to_comfyui.ps1 -ComfyUIPath "C:\path\to\ComfyUI"
	```

	If a target already exists, replace it with:

	```powershell
	.\scripts\link_to_comfyui.ps1 -ComfyUIPath "C:\path\to\ComfyUI" -Force
	```

4. Start ComfyUI and search for the node named "NativeImageSizes" in category "image/resolution".

## Repository layout

```text
.
├── __init__.py
├── nodes/
│   └── native_image_sizes.py
├── scripts/
│   └── link_to_comfyui.ps1
├── pyproject.toml
└── requirements-dev.txt
```

## Running lint

```powershell
ruff check .
ty check nodes
```

## Add a new node

1. Create a new module in `nodes/`, for example `nodes/image_nodes.py`.
2. Define the node implementation in that module.
3. Register node classes in top-level `comfy_entrypoint()` by returning them from `PluginExtension.get_node_list()` in `__init__.py`.
4. Use `define_schema()` on `io.ComfyNode` classes to set `node_id`, category, inputs, and outputs.

## Notes

- The link helper script attempts a symbolic link first, then falls back to a junction on Windows.
- This repository is intentionally minimal and ready for expansion into multiple node modules.