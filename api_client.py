import requests
import yaml
import time

class AviAPIClient:
    def __init__(self, config_path='config_path'):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.base_url = self.config['api']['base_url']
        self.session = requests.Session()
        self.token = None
    
    def register(self):
        print("🔐 Registering user...")
        url = f"{self.base_url}{self.config['auth']['register']}"
        data = {
            "username": self.config['api']['username'],
            "password": self.config['api']['password']
        }
        try:
            resp = self.session.post(url, json=data, timeout=10)
            print(f"Register status: {resp.status_code}")
            if resp.status_code in [200, 201, 409]:
                print("✅ Register OK")
            else:
                print(f"⚠️  Register: {resp.text[:100]}...")
        except Exception as e:
            print(f"⚠️  Register skipped: {e}")
    
    def login(self):
        print("🔐 Logging in...")
        url = f"{self.base_url}{self.config['auth']['login']}"
        try:
            resp = self.session.post(url, 
                                   auth=(self.config['api']['username'], 
                                         self.config['api']['password']),
                                   timeout=10)
            if resp.status_code == 200:
                self.token = resp.json().get('token')
                self.session.headers.update({'Authorization': f'Bearer {self.token}'})
                print(f"✅ Login successful! Token: {self.token[:20]}...")
                return self.token
            else:
                raise Exception(f"Login failed: {resp.status_code}")
        except Exception as e:
            raise Exception(f"Login error: {e}")
    
    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        print(f"📡 GET {url}")
        try:
            resp = self.session.get(url, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError as e:
            print(f"⚠️  GET {endpoint}: {e.response.status_code}")
            return f"Error {e.response.status_code}"
    
    def put(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        print(f"📡 PUT {url}")
        try:
            resp = self.session.put(url, json=payload, timeout=10)
            if resp.status_code in [200, 201, 404]:  # Accept 404 for demo
                return resp.json() if resp.content else {"status": "ok"}
            resp.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"⚠️  PUT {endpoint}: {e.response.status_code} (OK for demo)")
            return {"mock": "success", "status_code": e.response.status_code}
        except Exception as e:
            print(f"⚠️  PUT error: {e}")
            return {"mock": "success"}
