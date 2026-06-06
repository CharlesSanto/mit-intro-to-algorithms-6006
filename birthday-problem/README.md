# Birthday Matching Problem

## Description

This exercise from MIT 6.006 introduces the use of hash tables to efficiently find duplicate values in a collection.

The goal is to find the first birthday that appears more than once in a list.

## Example

**Input**

```python
["22-11", "22-11", "03-01", "15-05", "30-12"]
```

**Output**

```python
22-11
```

## Solution

The algorithm uses a `set` to keep track of birthdays that have already been seen.

For each birthday:

* If it is already in the set, return it.
* Otherwise, add it to the set.
* If no duplicate is found, return a message indicating that no match exists.

```python
def find_duplicate_birthday(classroom):

    seen_birthdays = set()

    for birthday in classroom:

        if birthday in seen_birthdays:
            return birthday

        seen_birthdays.add(birthday)

    return "No matching pair found"


test_classroom = ["22-11", "22-11", "03-01", "15-05", "30-12"]

result = find_duplicate_birthday(test_classroom)

print(f"Search result: {result}")
```

## Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(n)       |
| Space  | O(n)       |

The list is traversed only once, and lookups in a Python `set` take constant time on average.

## Comparison

| Approach           | Time Complexity |
| ------------------ | --------------- |
| Brute Force        | O(n²)           |
| Hash Table (`set`) | O(n)            |

## Key Concepts

* Hash Tables
* Python Sets
* Duplicate Detection
* Time Complexity Analysis
* Space Complexity Analysis

## Reference

MIT 6.006 – Introduction to Algorithms
