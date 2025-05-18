# Task 1: Git & Environment Setup

This folder is part of the Solar Challenge Week 1 project and documents the initial repository and environment setup.

## Objective

Set up version control and a reproducible Python environment for the project before starting data analysis.

## Steps Completed

1. **Repository Initialization**
   - Created a new GitHub repository: `solar-challenge-week1`.
   - Cloned the repository locally.

2. **Python Environment**
   - Set up a Python virtual environment using `venv`.
   - Added `requirements.txt` with all necessary dependencies.

3. **Version Control**
   - Created a branch called `setup-task`.
   - Made more than three meaningful commits:
     - `init: add .gitignore`
     - `chore: venv setup`
     - `ci: add GitHub Actions workflow`
   - Added a `.gitignore` file (ignores `data/`, `*.csv`, `.ipynb_checkpoints/`, and environment folders).

4. **Continuous Integration (CI)**
   - Added a GitHub Actions workflow (`.github/workflows/ci.yml`) that runs `pip install -r requirements.txt` and checks `python --version`.

5. **Documentation**
   - This `README.md` explains how to reproduce the environment and the initial setup process.

## How to Reproduce the Environment

1. **Clone the repository:**
   ```sh
   git clone https://github.com/matos-coder/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # Or
   source venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Check CI workflow:**
   - The GitHub Actions workflow will automatically run on push to verify the environment setup.

## Folder Structure

```
solar-challenge-week1/
├── .vscode/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
├── tests/
└── scripts/
```

## Key Performance Indicators (KPIs) Addressed

- Proper development environment setup
- Effective use of version control and branching
- Automated environment checks with CI

