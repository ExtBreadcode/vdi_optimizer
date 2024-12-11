import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger()

# utils/config.py
CONFIG = {
    "optimization_interval": 10  # in minutes
}