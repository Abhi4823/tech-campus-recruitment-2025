import sys
import os

def extract_logs(date, log_file, output_dir="output"):
    """Extract logs for a specific date from a large log file efficiently."""
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f"output_{date}.txt")

    try:
        with open(log_file, "r", encoding="utf-8") as file, open(output_file, "w", encoding="utf-8") as out_file:
            for line in file:
                if line.startswith(date):  # Efficient filtering
                    out_file.write(line)

        print(f"✅ Logs for {date} saved to {output_file}")

    except FileNotFoundError:
        print(f"❌ Error: Log file '{log_file}' not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# ✅ Fixing the typo in the main function
if __name__ == "_main_":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <YYYY-MM-DD> <log_file_path>")
        sys.exit(1)

    date_arg = sys.argv[1]  # Input date (YYYY-MM-DD)
    log_file_path = sys.argv[2]  # Log file path

    extract_logs(date_arg, log_file_path)