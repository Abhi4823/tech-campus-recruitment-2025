# Efficient Log Retrieval Solution

## 1️⃣ Problem Statement
Extract logs for a given date from a *1TB* log file efficiently.

## 2️⃣ Approaches Considered
1. *Loading entire file into memory* ❌ Not feasible due to size.
2. *Reading line-by-line and filtering* ✅ Best choice for efficiency.
3. *Using grep* ✅ Works but not cross-platform.
4. *Multi-threading* ✅ Could be used for very large files.

## 3️⃣ Final Solution
- Reads log *line by line* to save memory.
- Uses startswith(date) to *quickly filter logs*.
- *Saves logs to output/output_YYYY-MM-DD.txt*.

## 4️⃣ Steps to Run
```sh
python src/extract_logs.py 2024-12-01 /path/to/large_log_file.txt