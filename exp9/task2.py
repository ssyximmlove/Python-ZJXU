import os
import sys


def clean_directory(folder_path):
    extensions_to_delete = ['.tmp', '.log', '.obj', '.txt']
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.splitext(file)[1] in extensions_to_delete or os.path.getsize(file_path) == 0:
                    os.remove(file_path)
                    print(f"Deleted: '{file_path}'")
            except Exception as e:
                print(f"Error deleting '{file_path}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cleanup.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    clean_directory(folder_path)
    print("Cleanup complete.")
