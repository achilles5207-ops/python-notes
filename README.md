# 🐍 Python Notes

Personal Python notes, textbook-style comprehensive guides, and interactive practice code for my university course.

## 📂 Structure

```
python-notes/
├── .devcontainer/       # Dev container configuration
├── notes/               # Comprehensive textbook-style markdown notes by topic
├── notebooks/           # Interactive Jupyter notebooks for coding practice
├── scripts/             # Standalone Python scripts (like notebook generators)
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
# On Windows: .venv\Scripts\activate
# On Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
```

## 📝 Usage

- **Markdown notes** → Check the `notes/` folder for deeply detailed syllabus guides.
- **Jupyter notebooks** → Check the `notebooks/` folder to practice code with questions, solutions, and pro-tips!
- **Python scripts** → `scripts/` folder contains useful utility programs.
