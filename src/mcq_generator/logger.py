import logging  # Import the logging module to enable logging functionality in the script
import os  # Import the os module to interact with the operating system
from datetime import datetime  # Import the datetime class from the datetime module to work with date and time

# Create a log file name using the current date and time in the format MM_DD_YYYY_HH_MM_SS.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a directory path for logs by joining the current working directory with a folder named "logs"
log_path = os.path.join(os.getcwd(), "logs")

# Create the "logs" directory if it doesn't already exist
os.makedirs(log_path, exist_ok=True)

# Create the full file path for the log file by joining the log directory path with the log file name
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO to capture informational messages
    filename=LOG_FILEPATH,  # Specify the log file to write the logs to
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"  # Define the format for log messages
    # %(asctime)s: Timestamp of the log entry
    # %(lineno)d: Line number where the log entry was generated
    # %(name)s: Name of the logger
    # %(levelname)s: Log level (e.g., INFO, DEBUG, ERROR)
    # %(message)s: Log message
)
