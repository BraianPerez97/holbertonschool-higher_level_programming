#!/usr/bin/python3
import sys
from collections import defaultdict

counts = defaultdict(int)
sizes = 0
i = 0

try:
    for line in sys.stdin:
        i += 1
        parts = line.split()
        size = int(parts[-2])
        sizes += size
        code = parts[-3]
        counts[code] += 1

        if i % 10 == 0:
            print(f"File size: {sizes}")
            for code in sorted(counts):
                if counts[code] > 0:
                    print(f"{code}: {counts[code]}")

except KeyboardInterrupt:
    print(f"\nFile size: {sizes}")
    for code in sorted(counts):
        if counts[code] > 0:
            print(f"{code}: {counts[code]}")
