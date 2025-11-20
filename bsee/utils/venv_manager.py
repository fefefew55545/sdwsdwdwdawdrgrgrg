"""
Virtual Environment Handler for BSEE
Robust virtual environment management and package installation
"""

import os
import sys
import subprocess
import venv
from pathlib import Path

class VirtualEnvManager:
    """Manages virtual environments with error handling"""
    
    def __init__(self, venv_path=None):
        self.venv_path = venv_path or Path('bsee_venv')
        self.python_exe = None
        self.pip_exe = None
    
    def create_venv(self, force_recreate=False):
        """Create virtual environment with error handling"""
        try:
            if self.venv_path.exists() and not force_recreate:
                print(f'Virtual environment already exists at {self.venv_path}')
                return self._get_venv_executables()
            
            if force_recreate and self.venv_path.exists():
                import shutil
                shutil.rmtree(self.venv_path)
                print(f'Removed existing virtual environment')
            
            print(f'Creating virtual environment at {self.venv_path}...')
            venv.create(self.venv_path, with_pip=True, system_site_packages=False)
            
            return self._get_venv_executables()
            
        except Exception as e:
            raise Exception(f'Failed to create virtual environment: {e}')
    
    def _get_venv_executables(self):
        """Get paths to virtual environment executables"""
        if sys.platform == 'win32':
            self.python_exe = self.venv_path / 'Scripts' / 'python.exe'
            self.pip_exe = self.venv_path / 'Scripts' / 'pip.exe'
        else:
            self.python_exe = self.venv_path / 'bin' / 'python'
            self.pip_exe = self.venv_path / 'bin' / 'pip'
        
        if not self.python_exe.exists():
            raise Exception(f'Python executable not found: {self.python_exe}')
        
        return self.python_exe, self.pip_exe
    
    def install_package_with_retry(self, package_name, retries=3):
        """Install package with retry mechanism"""
        if not self.pip_exe:
            raise Exception('Virtual environment not initialized')
        
        for attempt in range(retries):
            try:
                print(f'Installing {package_name} (attempt {attempt + 1}/{retries})...')
                
                # Try installing with --user flag and --no-deps for problematic packages
                cmd = [
                    str(self.pip_exe), 'install',
                    package_name,
                    '--user',
                    '--no-deps',
                    '--timeout', '300'
                ]
                
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=600  # 10 minute timeout
                )
                
                if result.returncode == 0:
                    print(f'Successfully installed {package_name}')
                    return True
                else:
                    print(f'Installation failed: {result.stderr}')
                    
                    # Try alternative installation methods
                    if 'network' in result.stderr.lower():
                        return self._install_offline_fallback(package_name)
                    
            except subprocess.TimeoutExpired:
                print(f'Installation timeout for {package_name}')
                if attempt == retries - 1:
                    raise Exception(f'Timeout installing {package_name}')
            except Exception as e:
                if attempt == retries - 1:
                    raise Exception(f'Failed to install {package_name}: {e}')
        
        return False
    
    def _install_offline_fallback(self, package_name):
        """Try offline installation methods"""
        print(f'Trying offline installation for {package_name}...')
        
        # Try installing without version constraints
        fallback_cmd = [
            str(self.pip_exe), 'install',
            package_name,
            '--no-index',
            '--find-links', 'https://pypi.org/simple/',
            '--trusted-host', 'pypi.org'
        ]
        
        try:
            result = subprocess.run(fallback_cmd, capture_output=True, text=True)
            return result.returncode == 0
        except Exception:
            return False

def ensure_venv_and_dependencies():
    """Ensure virtual environment and basic dependencies are available"""
    manager = VirtualEnvManager()
    
    try:
        python_exe, pip_exe = manager.create_venv()
        print(f'✓ Virtual environment ready: {python_exe}')
        
        # Install basic required packages
        basic_packages = [
            'setuptools', 'wheel', 'pip'
        ]
        
        for package in basic_packages:
            try:
                manager.install_package_with_retry(package)
            except Exception as e:
                print(f'Warning: Could not install {package}: {e}')
        
        return True
        
    except Exception as e:
        print(f'Virtual environment setup failed: {e}')
        print('Falling back to system Python...')
        return False

if __name__ == '__main__':
    ensure_venv_and_dependencies()
