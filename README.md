# 🔗 Problem 4: Merging Custom-Formatted Lists with Position Overlap

## 🧩 Problem Statement

You are given two lists of strings in the format `"label:start-end"`.

Your task is to:
- Merge the ranges **label-wise** if the same label exists in both lists.
- For each label, include the range(s) from the list that contributes the **majority coverage**.
- If there's no overlap, combine both as separate entries.

---

## 📥 Input

Two lists:

```python
list1 = ["A:1-5", "B:10-15", "C:20-25"]
list2 = ["A:3-7", "B:11-13", "C:30-35"]

📤 Output
A merged list:
["A:1-7", "B:10-15", "C:20-25", "C:30-35"]
```

## ⚙️ Approach
- Parse both lists and group ranges by label.

- For labels present in both lists:

    - If ranges overlap or are adjacent, merge them into a single range.

    - If one list’s range fully contains the other, use that.

    - If both ranges are disjoint, include both.

- Preserve label ordering based on list1, then append unique labels from list2.

## 🚀 Sample Execution
```
merge_ranges(
  ["A:1-5", "B:10-15", "C:20-25"],
  ["A:3-7", "B:11-13", "C:30-35"]
)
Returns:
["A:1-7", "B:10-15", "C:20-25", "C:30-35"]
```

## 🛠️ How to Run
- Clone this repository.
- Run python merge_ranges.py or import the function and test with your own lists.

