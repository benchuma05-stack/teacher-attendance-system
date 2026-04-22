# PyInstaller script

import os
import sys

# Configuration
script_name = 'main.py'  # Change this to your main script
output_name = 'app.exe'   # Change this to your desired executable name

# Build the executable
if __name__ == '__main__':
    os.system(f'pyinstaller --onefile --name={output_name} {script_name}')
    print(f'{output_name} generated successfully!')
