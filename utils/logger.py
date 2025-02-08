import logging

# Configure logging
logging.basicConfig(
    filename="test_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_message(message):
    logging.info(message)
