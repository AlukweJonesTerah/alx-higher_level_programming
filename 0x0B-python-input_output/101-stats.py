#!/usr/bin/python3
"""
Real-time metrics computation for log data.

This script reads log entries from standard input, computes metrics
after every ten lines or upon a keyboard interruption (CTRL + C), and
prints statistics, including the total file size and count of
encountered status codes.

Usage:
    $ cat logfile.txt | ./metrics_script.py
"""


def print_metrics(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): Total file size up to the current point.
        status_codes (dict): Count of encountered status codes.
    """
    print("Total file size: {}".format(size))
    for code, count in sorted(status_codes.items()):
        print("Status {}: {}".format(code, count))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_counts = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(total_size, status_counts)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                status_code = parts[-2]
                if status_code in valid_codes:
                    status_counts[status_code] = status_counts.get(status_code, 0) + 1
            except IndexError:
                pass

        print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        raise
