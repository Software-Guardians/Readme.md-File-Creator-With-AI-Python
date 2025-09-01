import os
import json
import sys

# Dosya adları
CONFIG_FILE = "Config.json"
LICENSES_DIR = "Licenses"
OUTPUT_LICENSE_FILE = "../LICENSE"

def CreateLicense():
    # JSON dosyasını oku
    if not os.path.exists(CONFIG_FILE):
        print(f"❌ Error: {CONFIG_FILE} could not be found.")
        sys.exit(1)

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)

    license_name = config.get("license")
    if not license_name:
        print("❌ Error: The 'license' field could not be found in the JSON file.")
        sys.exit(1)

    # Lisans dosyasını bul
    license_file = os.path.join(LICENSES_DIR, f"{license_name}.txt")

    if not os.path.exists(license_file):
        print(f"❌ Error: {license_file} could not be found.")
        sys.exit(1)

    # Lisans içeriğini oku
    with open(license_file, "r", encoding="utf-8") as f:
        license_content = f.read()

    # LICENSE dosyasına yaz
    with open(OUTPUT_LICENSE_FILE, "w", encoding="utf-8") as f:
        f.write(license_content)

    print(f"✅ The {license_name} license has been written to the '{OUTPUT_LICENSE_FILE}' file.")

if __name__ == "__main__":
    CreateLicense()
