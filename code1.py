import os
hostname = "google.com"
response = os.system(f"ping -c 1 {hostname}")
if response == 0:
    print(f"{hostname} is online.")
else:
    print(f"{hostname} is offline.")

