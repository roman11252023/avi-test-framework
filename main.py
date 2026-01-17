from test_runner import TestRunner
from concurrent.futures import ThreadPoolExecutor  # BUILT-IN MODULE
import time

def run_parallel_tests():
    print("🧵 Running PARALLEL tests...")
    
    # Create 2 test runners (parallel execution)
    with ThreadPoolExecutor(max_workers=2) as executor:
        test1 = executor.submit(TestRunner('config.yaml').run_test)
        test2 = executor.submit(TestRunner('config.yaml').run_test)
        
        # Wait for both to complete
        test1.result()
        test2.result()
    print("✅ All parallel tests completed!")

if __name__ == "__main__":
    print("VMware Avi Load Balancer Test Framework")
    print("=====================================")
    run_parallel_tests()
