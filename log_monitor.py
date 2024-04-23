import subprocess
import signal
import sys
import logging
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='log_monitor.log')

# Global variables
log_file = "C:\\Users\\Arun\\log_monitor.log"
keywords_to_count = ['error', 'HTTP']  # Keywords to count occurrences
summary_report_size = 5  # Size of summary report


def monitor_log():
    try:
        logging.info("Monitoring log file: %s", log_file)
        tail_process = subprocess.Popen(['tail', '-n', '0', '-F', log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                         text=True, preexec_fn=subprocess.os.setpgrp)
        signal.signal(signal.SIGINT, signal_handler)
        for line in tail_process.stdout:
            logging.debug("New log entry: %s", line.strip())
            analyze_log_entry(line.strip())
    except Exception as e:
        logging.error("Error occurred while monitoring log file: %s", e)


def analyze_log_entry(log_entry):
    # Perform analysis on the log entry
    # For example, counting occurrences of specific keywords or patterns
    for keyword in keywords_to_count:
        if keyword.lower() in log_entry.lower():
            logging.warning("Keyword '%s' found in log entry: %s", keyword, log_entry)

    # Further analysis can be added as needed


def generate_summary_report():
    try:
        with open(log_file, 'r') as file:
            log_entries = file.readlines()
            keywords_count = Counter()

            for entry in log_entries:
                for keyword in keywords_to_count:
                    if keyword.lower() in entry.lower():
                        keywords_count[keyword] += 1

            if keywords_count:
                logging.info("Generating summary report:")
                sorted_keywords_count = keywords_count.most_common(summary_report_size)
                for keyword, count in sorted_keywords_count:
                    logging.info("Keyword: %s, Count: %d", keyword, count)
            else:
                logging.info("No keywords found in log entries for generating summary report.")
    except FileNotFoundError:
        logging.error("Log file '%s' not found.", log_file)


def signal_handler(sig, frame):
    logging.info("Received signal %s. Exiting.", sig)
    sys.exit(0)


def main():
    monitor_log()


if __name__ == "__main__":
    main()
