# add installed python pkgs
import zipfile
import os

def unzip_file(zip_file_path, extract_dir):
    # Create the extraction directory if it does not exist
    os.makedirs(extract_dir, exist_ok=True)

    try:
        # Open the ZIP file for reading
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Extract all contents of the ZIP file to the extraction directory
            zip_ref.extractall(extract_dir)
            print(f"Files extracted to: {extract_dir}")
    except zipfile.BadZipFile:
        print(f"Error: Invalid ZIP file: {zip_file_path}")
    except FileNotFoundError:
        print(f"Error: File not found: {zip_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    zip_file_path = 'path/to/your/archive.zip'
    extract_dir = 'path/to/extract/directory'

    unzip_file(zip_file_path, extract_dir)

