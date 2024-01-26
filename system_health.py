import psutil
import logging
import os

CPU_THRESHOLD = 2
MEMORY_THRESHOLD = 2
DISK_THRESHOLD = 2


LOG_FILE = "/Users/aniketdubey/Desktop/Accunox/1 System Health Monitoring Script/system_health.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    logging.info(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU Usage! Current usage: {cpu_usage}%")


def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    logging.info(f"Memory Usage: {memory_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory Usage! Current usage: {memory_usage}%")
    else:
        logging.info("Memory usage within normal range.")


def check_disk_space():
    disk_usage = psutil.disk_usage('/').percent
    logging.info(f"Disk Space Usage: {disk_usage}%")
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"Low Disk Space! Current usage: {disk_usage}%")


def check_running_processes():
    running_processes = psutil.process_iter()
    logging.info("Running Processes:")
    for process in running_processes:
        logging.info(f" - {process.name()} (PID: {process.pid})")


def main():
    logging.info("System Health Monitoring Script started.")

    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_running_processes()

    logging.info("System Health Monitoring Script completed.")


if __name__ == "__main__":
    main()
