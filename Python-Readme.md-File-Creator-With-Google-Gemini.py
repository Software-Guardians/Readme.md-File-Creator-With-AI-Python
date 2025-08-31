import os
import json
import sys
import google.generativeai as genai

# JSON dosyasını oku
CONFIG_FILE = "Python-Readme.md-Creator-Config.json"
SCRIPT_FILE = "Python-Readme.md-File-Creator-With-Google-Gemini.py"

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

project_name = config.get("project_name", "Unnamed Project")
topic = config.get("topic", "No topic specified")
description = config.get("description", "No description provided.")
YOUR_API_KEY = config.get("API", "").strip()
features = config.get("features", [])
installation = config.get("installation", [])
usage = config.get("usage", [])
contribution = config.get("contribution", "No contribution info provided.")
license_name = config.get("license", "No license specified.")
languages = config.get("languages", ["en"])
ignore_list = config.get("ignore", [])

# API key kontrolü
if not YOUR_API_KEY:
    print("❌ API key has not been provided. Please add your API key in the JSON config.")
    sys.exit(1)

# Mevcut çalışma klasörü
current_dir = os.path.abspath(os.getcwd())

# Proje klasöründeki dosya ve klasörleri al (config, script ve ignore edilenleri hariç tut)
project_files = []
for root, dirs, files in os.walk("."):
    # ignore edilen klasörleri tamamen atla
    dirs[:] = [d for d in dirs if os.path.relpath(os.path.join(root, d)) not in ignore_list]

    for d in dirs:
        path = os.path.relpath(os.path.join(root, d))
        if path not in [CONFIG_FILE, SCRIPT_FILE] and path not in ignore_list:
            project_files.append(path)

    for file in files:
        path = os.path.relpath(os.path.join(root, file))
        if path not in [CONFIG_FILE, SCRIPT_FILE] and path not in ignore_list:
            project_files.append(path)

# Eğer klasörde yalnızca config ve script varsa README oluşturmayı atla
if not project_files:
    print("ℹ️ No project files found (excluding config, script, and ignored). README generation skipped.")
    sys.exit(0)

project_file_tree = "\n".join(project_files)

# Google Gemini API anahtarını ayarla
genai.configure(api_key=YOUR_API_KEY)

# Model seçimi
model = genai.GenerativeModel("gemini-2.5-flash")

# README.md içeriğini birleştirecek değişken
final_readme = f"# {project_name}\n\n"

# Her dil için prompt gönder ve sonucu ekle
for lang in languages:
    prompt = f"""
You are an expert AI technical writer. Create a professional and visually appealing README.md
for a GitHub project, in the language: {lang}.

Project info:
- Name: {project_name}
- Topic: {topic}
- Description: {description}
- Features: {', '.join(features) if features else 'No features provided.'}
- Installation: {', '.join(installation) if installation else 'No installation steps provided.'}
- Usage: {', '.join(usage) if usage else 'No usage info provided.'}
- Contribution: {contribution}
- License: {license_name}

Project file structure:
{project_file_tree}

Project directory:
{current_dir}

Rules:
1. Include all relevant sections (Description, Features, Installation, Usage, Contribution, License, Project Structure).
2. If some sections are missing, generate content intelligently based on project topic.
3. Format with Markdown: headings, lists, code blocks, emojis, badges.
4. Output the README content as plain Markdown (do NOT wrap it in triple backticks or markdown code fences).
5. The output must be ready to be saved directly as a README.md file without extra wrappers.
"""

    try:
        response = model.generate_content(prompt)
        readme_content = response.text.strip()

        # Güvenlik: Başta/sonda yanlışlıkla gelen ``` bloklarını temizle
        if readme_content.startswith("```"):
            readme_content = readme_content.split("\n", 1)[1]
        if readme_content.endswith("```"):
            readme_content = readme_content.rsplit("\n", 1)[0]

    except Exception as e:
        print(f"❌ Failed to generate README: {e}")
        sys.exit(1)

    # Dil başlığı ekleyip final_readme'e ekle
    final_readme += f"\n---\n\n## {lang.upper()}\n\n{readme_content}\n"

# README.md dosyasına yaz
with open("README.md", "w", encoding="utf-8") as f:
    f.write(final_readme)

print("✅ README.md file created with Google Gemini")
