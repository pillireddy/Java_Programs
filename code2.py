import shutil
original = "important.txt"
backup = "important_backup.txt"
shutil.copy(original, backup)
print(f"Backup of {original} created as {backup}.")

