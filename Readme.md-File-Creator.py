import os
import json
import sys
import google.generativeai as genai

# JSON dosyasını oku
CONFIG_FILE = "Config.json"
SCRIPT_FILE = "Readme.md-File-Creator.py"

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

# Yeni eklenen alanlar
github_repository = config.get("github_repository", "").strip()
author = config.get("Author", "").strip()
date = config.get("Date", "").strip()

# Zorunlu alan kontrolleri
if not YOUR_API_KEY:
    print("❌ API key has not been provided. Please add your API key in the JSON config.")
    sys.exit(1)

if not github_repository:
    print("❌ GitHub repository URL has not been provided. Please add 'github_repository' in the JSON config.")
    sys.exit(1)

if not author:
    print("❌ Author has not been provided. Please add 'Author' in the JSON config.")
    sys.exit(1)

# Mevcut çalışma klasörü (script'in bulunduğu)
current_dir = os.path.abspath(os.getcwd())
parent_dir = os.path.dirname(current_dir)  # Bir üst klasör

# Proje klasöründeki dosya ve klasörleri al (config, script ve ignore edilenleri hariç tut)
project_files = []
for root, dirs, files in os.walk(parent_dir):
    # ignore edilen klasörleri tamamen atla
    dirs[:] = [d for d in dirs if os.path.relpath(os.path.join(root, d), parent_dir) not in ignore_list]

    for d in dirs:
        path = os.path.relpath(os.path.join(root, d), parent_dir)
        if path not in [CONFIG_FILE, SCRIPT_FILE] and path not in ignore_list:
            project_files.append(path)

    for file in files:
        path = os.path.relpath(os.path.join(root, file), parent_dir)
        if path not in [CONFIG_FILE, SCRIPT_FILE] and path not in ignore_list:
            project_files.append(path)

# Eğer klasörde yalnızca config ve script varsa README oluşturmayı atla
if not project_files:
    print("ℹ️ No project files found (excluding config, script, and ignored). README generation skipped.")
    sys.exit(0)

project_file_tree = "\n".join(project_files)

# Google Gemini API anahtarını ayarla
genai.configure(api_key=YOUR_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# Kod bloğu kontrol ve düzeltme fonksiyonu
def fix_code_blocks(text: str) -> str:
    """
    Eğer README içeriğinde ``` ile başlayan ama kapanmayan kod blokları varsa
    sonuna ``` ekler.
    """
    if not text:
        return text
    open_count = text.count("```")
    if open_count % 2 != 0:
        text += "\n```"
    return text.strip()

# README.md içeriğini oluşturacak değişken
final_readme = f"# {project_name}\n\n"

# İlk dil (ana dil) ile içerik oluştur
main_lang = languages[0]

prompt_main = f"""
You are an expert AI technical writer. Create a professional and visually appealing README.md
for a GitHub project, in the language: {main_lang}.

Project info:
- Name: {project_name}
- Topic: {topic}
- Description: {description}
- Features: {', '.join(features) if features else 'No features provided.'}
- Installation: {', '.join(installation) if installation else 'No installation steps provided.'}
- Usage: {', '.join(usage) if usage else 'No usage info provided.'}
- Contribution: {contribution}
- License: {license_name}
- GitHub Repository: {github_repository}
- Author: {author}
- Date: {date if date else 'Not specified'}

Project file structure:
{project_file_tree}

Project directory:
{parent_dir}

Rules:
1. Include all relevant sections (Description, Features, Installation, Usage, Contribution, License, Project Structure, Repository, Author, Date).
2. If some sections are missing, generate content intelligently based on project topic.
3. Format with Markdown: headings, lists, code blocks, emojis, badges.
4. Output the README content as plain Markdown (do NOT wrap it in triple backticks or markdown code fences).
5. The output must be ready to be saved directly as a README.md file without extra wrappers.
"""

try:
    response_main = model.generate_content(prompt_main)
    main_content = response_main.text.strip()

    # Güvenlik: Başta/sonda ``` bloklarını temizle
    if main_content.startswith("```"):
        main_content = main_content.split("\n", 1)[1]
    if main_content.endswith("```"):
        main_content = main_content.rsplit("\n", 1)[0]

    # Kod bloklarını kapat
    main_content = fix_code_blocks(main_content)

except Exception as e:
    print(f"❌ Failed to generate README: {e}")
    sys.exit(1)

# Ana dili README'ye ekle
final_readme += f"## {main_lang.upper()}\n\n{main_content}\n"

# Diğer dillere çeviri yap
for lang in languages[1:]:
    prompt_translate = f"""
Translate the following README content into {lang} while preserving formatting, headings, lists, code blocks, emojis, and badges.
Do NOT change the content, only translate the text.

Content to translate:
{main_content}
"""

    try:
        response_translate = model.generate_content(prompt_translate)
        translated_content = response_translate.text.strip()

        # Güvenlik: Başta/sonda ``` bloklarını temizle
        if translated_content.startswith("```"):
            translated_content = translated_content.split("\n", 1)[1]
        if translated_content.endswith("```"):
            translated_content = translated_content.rsplit("\n", 1)[0]

        # Kod bloklarını kapat
        translated_content = fix_code_blocks(translated_content)

        final_readme += f"\n---\n\n## {lang.upper()}\n\n{translated_content}\n"

    except Exception as e:
        print(f"❌ Failed to translate README to {lang}: {e}")
        continue

# README.md dosyasına yaz
with open("../README.md", "w", encoding="utf-8") as f:
    f.write(final_readme)

print("✅ README.md file created with Google Gemini (with translations)")
