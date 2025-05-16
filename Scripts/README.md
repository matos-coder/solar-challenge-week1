# Solar Challenge Week 1 - Scripts

## Task 1: Git & Environment Setup

This repository contains the initial setup for the Solar Challenge Week 1 project. The following steps were completed:

### 1. Repository Initialization

- Created a new GitHub repository: `solar-challenge-week1`
- Cloned the repository locally

### 2. Python Environment Setup

- Created a Python virtual environment using `venv`
- Added a `requirements.txt` file for dependencies

### 3. Branching & Commits

- Created a branch named `setup-task`
- Made these commits:
    - `init: add .gitignore`
    - `chore: venv setup`
    - `ci: add GitHub Actions workflow`

### 4. .gitignore

- Added `.gitignore` to exclude:
    - `data/`
    - Any `.csv` files
    - `.ipynb_checkpoints/`

### 5. Continuous Integration

- Added a GitHub Actions workflow at `.github/workflows/ci.yml`
- Workflow runs `pip install -r requirements.txt` and/or `python --version` to verify environment setup

---

## How to Reproduce the Environment

1. **Clone the repository:**
     ```bash
     git clone https://github.com/matos-coder/solar-challenge-week1.git
     cd solar-challenge-week1
     ```

2. **Create and activate a virtual environment:**
     ```bash
     python -m venv venv
     ```

3. **Install dependencies:**
     ```bash
     pip install -r requirements.txt
     ```

