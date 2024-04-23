# Log Monitor Script

## Overview
This script is designed to monitor a specified log file in real-time, perform basic analysis on log entries, and generate summary reports based on predefined keywords.

## Prerequisites
- Python 3.x installed on your system.

## Dependencies
- No external dependencies beyond the Python standard library.

## Usage
1. Clone or download the `log_monitor.py` script to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the `log_monitor.py` script.

4. Run the script using the following command:

5. The script will start monitoring the specified log file (`filename.log` by default) and display any new log entries in real-time.

6. Press `Ctrl+C` to stop the monitoring loop and exit the script.

7. Optionally, you can customize the log file path, keywords to count, and summary report size by modifying the variables in the script.

## Testing
1. Run the script as described in the "Usage" section.

2. Verify that the script starts monitoring the log file and displays new log entries in the terminal.

3. Check the `log_monitor.log` file in the specified location to ensure that log messages are being recorded.


## Notes
- Ensure that the specified log file exists in the specified location before running the script.
- Make sure to have necessary permissions to read the log file.
- Customize the script according to your specific requirements, such as modifying log file paths or adding additional analysis functionalities.

