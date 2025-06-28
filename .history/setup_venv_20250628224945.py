import os
import subprocess
import sys

project_dir = os.path.dirname(os.path.abspath(__file__))
venv_dir = os.path.join(project_dir, '.venv')

# Step 1: Create .venv if it doesn't exist
if not os.path.exists(venv_dir):
    print("🔧 Creating virtual environment...")
    subprocess.check_call([sys.executable, "-m", "venv", venv_dir])

# Step 2: Activate venv and install dependencies
pip_path = os.path.join(venv_dir, 'Scripts', 'pip.exe')  # For Windows

# Step 2a: Generate requirements.txt if missing (optional)
if not os.path.exists(os.path.join(project_dir, 'requirements.txt')):
    print("📦 No requirements.txt found. Generating with pipreqs...")
    subprocess.check_call([pip_path, "install", "pipreqs"])
    subprocess.check_call([os.path.join(venv_dir, 'Scripts', 'python.exe'), "-m", "pipreqs", project_dir, "--force"])

# Step 2b: Install dependencies
print("📦 Installing packages...")
subprocess.check_call([pip_path, "install", "-r", os.path.join(project_dir, "requirements.txt")])

# # Step 3: Optionally run your main script
# script_to_run = os.path.join(project_dir, "batch_scrapping.py")
# print(f"🚀 Running {script_to_run}")
# subprocess.check_call([os.path.join(venv_dir, 'Scripts', 'python.exe'), script_to_run])
