# 🐍 Python Notes

Personal Python notes and code examples for my university course.

## 📂 Structure

```
python-notes/
├── .devcontainer/       # Dev container configuration
├── notes/               # Markdown notes by topic
├── notebooks/           # Jupyter notebooks for practice
├── scripts/             # Standalone Python scripts
└── requirements.txt     # Project dependencies
```

## 🚀 Getting Started

### Using Dev Container (Recommended)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Install the **Dev Containers** extension in VS Code
3. Open this folder in VS Code
4. Click **"Reopen in Container"** when prompted (or use `Ctrl+Shift+P` → `Dev Containers: Reopen in Container`)
5. Wait for the container to build — all dependencies will be installed automatically

### Local Setup (Alternative)

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## 📝 Usage

- **Markdown notes** → `notes/` folder
- **Jupyter notebooks** → `notebooks/` folder
- **Python scripts** → `scripts/` folder
