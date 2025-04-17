log_file = "example.log"
try:
    with open(log_file, "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print(f"{log_file} not found. Please create it first.")

