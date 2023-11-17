#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""

import sys

def print_metrics(total_size, status_codes):
    """
    Prints metrics based on the current statistics.

    Parameters:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing counts for each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def main():
    """
    Main function to read stdin, compute metrics, and print statistics.
    """
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) >= 2:
                status_code = parts[-2]
                total_size += int(parts[-1])
                if status_code in status_codes:
                    status_codes[status_code] += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
