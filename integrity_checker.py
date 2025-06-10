import hashlib
import os

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def save_original_hash(file_path, output_file="original_hash.txt"):
    hash_value = calculate_sha256(file_path)
    with open(output_file, "w") as f:
        f.write(hash_value)
    print(f"✅ Hash saved in {output_file}")

def verify_file(file_path, hash_file="original_hash.txt"):
    if not os.path.exists(hash_file):
        print("❌ Hash file not found. Run in save mode first.")
        return
    with open(hash_file, "r") as f:
        original_hash = f.read().strip()

    current_hash = calculate_sha256(file_path)
    if current_hash == original_hash:
        print("✅ File is original and not modified.")
    else:
        print("⚠️ WARNING: File integrity check FAILED!")

if __name__ == "__main__":
    print("=== File Integrity Checker ===")
    print("1. Save original hash")
    print("2. Verify file integrity")
    choice = input("Choose option (1/2): ")

    path = input("Enter full file path: ")

    if choice == "1":
        save_original_hash(path)
    elif choice == "2":
        verify_file(path)
    else:
        print("❌ Invalid choice.")
