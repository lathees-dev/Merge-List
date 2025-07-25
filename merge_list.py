from collections import defaultdict


def parse_range(entry):
    label, range_part = entry.split(":")
    start, end = map(int, range_part.split("-"))
    return label, start, end


def format_range(label, start, end):
    return f"{label}:{start}-{end}"


def overlap_enough(a_start, a_end, b_start, b_end):
    overlap = max(0, min(a_end, b_end) - max(a_start, b_start) + 1)
    min_len = min(a_end - a_start + 1, b_end - b_start + 1)
    return (overlap / min_len) >= 0.5


def merge_custom_ranges(list1, list2):
    all_ranges = defaultdict(list)

    for entry in list1 + list2:
        label, start, end = parse_range(entry)
        all_ranges[label].append((start, end))

    result = []

    for label, ranges in all_ranges.items():
        ranges.sort()
        merged = []

        for start, end in ranges:
            if not merged:
                merged.append((start, end))
                continue

            last_start, last_end = merged[-1]

            if overlap_enough(last_start, last_end, start, end):
                merged[-1] = (min(last_start, start), max(last_end, end))
            else:
                merged.append((start, end))

        result.extend([format_range(label, s, e) for s, e in merged])

    return result

if __name__ == "__main__":
    list1 = ["A:1-5", "B:10-20"]
    list2 = ["A:3-7", "B:15-25", "C:5-10"]

    print(merge_custom_ranges(list1, list2))
    # Output: ['A:1-7', 'B:10-25', 'C:5-10']
