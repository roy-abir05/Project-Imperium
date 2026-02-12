import time
import sys
import logging
import random

# Configure logging
logging.basicConfig(
    filename='app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - [TradeFlowEngine] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def run_server():
    print("TradeFlow Engine v2.1 Starting...")
    logging.info("System startup initiated. Memory Arena: 4GB allocated.")
    time.sleep(1)
    logging.info("Network Interface bound to port 8080.")
    print("System Online. Processing Orders...")

    orders_processed = 0
    
    try:
        while True:
            time.sleep(1)
            orders_processed += 1
            
            # CHANGE THIS TO 'True' TO CRASH THE SERVER FOR THE DEMO
            SIMULATE_CRASH = False 
            
            if SIMULATE_CRASH:
                error_msg = "CRITICAL: Segfault in matching_engine.cpp:402 - Memory Arena Overflow"
                logging.error(error_msg)
                print(f"{error_msg}")
                raise RuntimeError("Engine Crash")
            
            if orders_processed % 5 == 0:
                logging.info(f"Heartbeat: Processed {orders_processed} orders. Latency: {random.randint(2, 15)}ms")
                print(f"[{orders_processed}] Orders processed... (Stable)")
                
    except Exception as e:
        logging.critical("System Shutdown due to fatal error.")
        sys.exit(1)

if __name__ == "__main__":
    run_server()