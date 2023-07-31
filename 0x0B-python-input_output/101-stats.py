#!/usr/bin/env python3

import sys
from collections import defaultdict


def compute_metrics():
    """Reads standard input line by line and computes metrics.

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
        Total file size: File size: <total size>
        where is the sum of all previous (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear, don’t print anything for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order
    """

    # Initialize counters and dictionaries
    total_file_size = 0
    status_codes = defaultdict(int)

    try:
        for i, line in enumerate(sys.stdin):
            # Split the line into its components
            components = line.split()

            # Extract the file size and status code
            file_size = int(components[-1])
            status_code = int(components[-2])

            # Update the counters and dictionaries
            total_file_size += file_size
            status_codes[status_code] += 1

            # Print the metrics every 10 lines
            if i > 0 and (i + 1) % 10 == 0:
                print("File size: {}".format(total_file_size))
                for code in sorted(status_codes.keys()):
                    print("{}: {}".format(code, status_codes[code]))

    except KeyboardInterrupt:
        pass

    # Print the final metrics
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    compute_metrics()
