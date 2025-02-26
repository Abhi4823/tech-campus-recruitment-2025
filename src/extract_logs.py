import sys

print("Script Started")  # Debugging message

if len(sys.argv) != 3:
    print("Usage: python extract_logs.py <date> <log_file_path>")
    sys.exit(1)

date = sys.argv[1]
log_file_path = sys.argv[2]

print(f"Filtering logs for date: {date}")
print(f"Reading log file: {log_file_path}")

try:
    with open(log_file_path, "r") as file:
        logs = [line for line in file if date in line]
        print(f"Found {len(logs)} matching logs")  # Debugging message

        if logs:
            with open(f"output/output_{date}.txt", "w") as output_file:
                output_file.writelines(logs)
            print(f"Logs saved to output/output_{date}.txt")
        else:
            print("No logs found for this date.")

except Exception as e:
    print(f"Error: {e}")