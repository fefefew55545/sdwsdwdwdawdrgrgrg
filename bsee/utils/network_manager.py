"""
Network Utilities for BSEE
Provides robust network handling and error recovery
"""

import urllib.request
import urllib.error
import socket
import ssl
import time

class NetworkManager:
    """Manages network operations with error handling"""
    
    def __init__(self, timeout=30, retries=3):
        self.timeout = timeout
        self.retries = retries
        self.setup_ssl_context()
    
    def setup_ssl_context(self):
        """Setup SSL context for secure connections"""
        try:
            self.ssl_context = ssl.create_default_context()
            self.ssl_context.check_hostname = False
            self.ssl_context.verify_mode = ssl.CERT_NONE
        except Exception:
            self.ssl_context = None
    
    def download_with_retry(self, url, filepath):
        """Download file with retry mechanism"""
        for attempt in range(self.retries):
            try:
                return self._download_once(url, filepath)
            except Exception as e:
                if attempt == self.retries - 1:
                    raise e
                print(f'Download attempt {attempt + 1} failed, retrying...')
                time.sleep(2 ** attempt)  # Exponential backoff
    
    def _download_once(self, url, filepath):
        """Download file once"""
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'BSEE/1.0'}
            )
            
            with urllib.request.urlopen(req, timeout=self.timeout, context=self.ssl_context) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.read())
            
            return True
            
        except urllib.error.URLError as e:
            raise Exception(f'Network error downloading {url}: {e}')
        except socket.timeout:
            raise Exception(f'Timeout downloading {url}')
        except Exception as e:
            raise Exception(f'Error downloading {url}: {e}')
    
    def check_internet_connection(self):
        """Check if internet connection is available"""
        try:
            # Try to connect to a reliable server
            socket.create_connection(('8.8.8.8', 53), timeout=5)
            return True
        except Exception:
            return False

def check_network_dependencies():
    """Check if network dependencies are available"""
    manager = NetworkManager()
    
    if not manager.check_internet_connection():
        print('Warning: No internet connection available')
        print('Some features may not work without internet access')
        return False
    
    return True

if __name__ == '__main__':
    check_network_dependencies()
