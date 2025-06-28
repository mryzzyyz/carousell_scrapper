import os
import subprocess
import sys

# Paths
project_dir = os.path.dirname(os.path.abspath(__file__))
venv_dir = os.path.join(project_dir, '.venv')
python_exe = os.path.join(venv_dir, 'Scripts', 'python.exe')
pip_exe = os.path.join(venv_dir, 'Scripts', 'pip.exe')
requirements_path = os.path.join(project_dir, 'requirements.txt')
main_script = os.path.join(project_dir, 'batch_scrapping.py')

# Step 1: Create .venv if it doesn't exist
if not os.path.exists(venv_dir):
    print("🔧 Creating virtual environment...")
    subprocess.check_call([sys.executable, "-m", "venv", venv_dir])

# Step 2: Upgrade pip and install build tools
print("📦 Ensuring core build tools are available...")
subprocess.check_call([python_exe, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel", "Cython"])

# Step 3: Install dependencies
if os.path.exists(requirements_path):
    print("📦 Installing from requirements.txt...")
    try:
        subprocess.check_call([pip_exe, "install", "-r", requirements_path])
    except subprocess.CalledProcessError as e:
        print("⚠️ Error while installing dependencies.")
        print("   → Consider checking requirements.txt for heavy packages like `pyjnius`, or use minimal requirements.")
        sys.exit(1)
else:
    print("⚠️ No requirements.txt found. You can generate one using pipreqs.")

# Step 4: Run the main script
print(f"🚀 Running {main_script}")
subprocess.check_call([python_exe, main_script])
