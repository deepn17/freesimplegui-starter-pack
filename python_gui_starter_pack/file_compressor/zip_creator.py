import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    """
    Create a zip archive from a list of file paths.
    
    Args:
        filepaths: List of file paths to include in the archive
        dest_dir: Destination directory where the zip file will be created
        
    Returns:
        Path object pointing to the created zip file
    """
    dest_path = pathlib.Path(dest_dir) / "compressed.zip"
    pathlib.Path(dest_dir).mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            p = pathlib.Path(filepath)
            print(f"Looking for: {p}")
            print(f"Absolute path: {p.absolute()}")
            print(f"Exists: {p.exists()}")
            
            if p.exists():
                # Use absolute path to ensure file is found
                # Use the filename as arcname to avoid including full path in zip
                archive.write(p.absolute(), arcname=p.name)
                print(f"✓ Added: {filepath}")
            else:
                print(f"✗ File not found: {filepath}")

    print(f"Zip file created at: {dest_path.absolute()}")
    return dest_path


if __name__ == "__main__":
    # Test the function with debug output
    print("Testing make_archive function...")
    result = make_archive(['../cli.py'], '../file_compressor/dest')
    print(f"\nResult: {result}")
