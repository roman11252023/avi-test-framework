# VMware Avi Load Balancer Test Automation Framework

## ✅ Features Implemented
- **YAML Configuration-driven** API endpoints & credentials
- **Parallel Execution** using `ThreadPoolExecutor` (2+ concurrent tests)
- **4-Stage Test Workflow**: Pre-Fetch → Pre-Validation → Trigger → Post-Validation
- **Live Mock API Integration**: Registration/Login/Token-based auth
- **Robust Error Handling**: Mock fallbacks + timeout handling

## 🎯 Test Workflow
1. **Pre-Fetcher**: Fetches tenants(1), virtual services(25), service engines(25)
2. **Pre-Validation**: Finds "backend-vs-t1r_1000-1", validates `enabled: true`
3. **Trigger**: PUT `/api/virtualservice/{uuid}` with `{"enabled": false}`
4. **Post-Validation**: GET verifies `enabled: false`

## 🚀 Quick Start
```bash
pip install -r requirements.txt
# Update config.yaml with your credentials
python main.py
