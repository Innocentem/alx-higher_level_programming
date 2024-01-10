#!/usr/bin/python3

import sys
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print(f'Total file size: {total_size}')
    for code in sorted(status_counts):
        print(f'{code}: {status_counts[code]}')

def main():
    total_size = 0
    status_counts = defaultdict(int)
    lines_read = 0

    try:
        for line in sys.stdin:
            lines_read += 1

            # Parse the input line
            parts = line.split()
            if len(parts) >= 10:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size
                status_counts[status_code] += 1

            # Print statistics every 10 lines
            if lines_read % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()

