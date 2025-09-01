# 🤖 AI-Powered README & License Creator

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)](https://ai.google.dev/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/Software-Guardians/Readme.md-File-Creator-With-AI-Python)

**Author:** Emrullah Enis Çetinkaya  
**Repository:** [Software-Guardians/Readme.md-File-Creator-With-AI-Python](https://github.com/Software-Guardians/Readme.md-File-Creator-With-AI-Python)

---

## 🌟 ENGLISH

### 📖 Description

**AI-Powered README & License Creator** is an intelligent Python tool that automatically generates professional README.md files and LICENSE files for your projects using Google Gemini AI. Simply configure your project details in a JSON file, and let AI create comprehensive documentation with multi-language support!

### ✨ Features

- 🤖 **AI-Generated Content**: Uses Google Gemini 2.5 Flash for intelligent README generation
- 🌍 **Multi-Language Support**: Generate README in multiple languages (English, Turkish, and more)
- 📄 **Automatic License Creation**: Supports multiple license types including MIT, Apache, GPL, and more
- 🔧 **Smart Project Analysis**: Automatically scans project structure and files
- ⚙️ **JSON Configuration**: Easy-to-use configuration system
- 🎨 **Beautiful Formatting**: Professional markdown with emojis, badges, and proper structure
- 🚫 **Intelligent Filtering**: Automatically ignores common files like `.git`, `venv`, `__pycache__`
- 🔄 **One-Click Generation**: Run everything with a single command

### 🚀 Installation

#### Prerequisites
- Python 3.7 or higher
- Google Gemini API key ([Get it here](https://ai.google.dev/))

#### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Software-Guardians/Readme.md-File-Creator-With-AI-Python.git
   cd Readme.md-File-Creator-With-AI-Python
   ```

2. **Install required packages:**
   ```bash
   pip install google-generativeai
   ```

3. **Get your Google Gemini API key:**
   - Visit [Google AI Studio](https://ai.google.dev/)
   - Create an account and generate an API key
   - Keep it secure for configuration

### ⚙️ Configuration

Edit the `Config.json` file with your project details:

```json
{
  "project_name": "Your Project Name",
  "github_repository": "https://github.com/yourusername/yourproject",
  "Author": "Your Full Name",
  "Date": "2024-01-01",
  "topic": "Brief project topic",
  "description": "Detailed project description",
  "API": "your-gemini-api-key-here",
  "features": [
    "Feature 1",
    "Feature 2",
    "Feature 3"
  ],
  "installation": [
    "Step 1: Clone repository",
    "Step 2: Install dependencies",
    "Step 3: Configure settings"
  ],
  "usage": [
    "Usage example 1",
    "Usage example 2"
  ],
  "contribution": "Guidelines for contributing to the project.",
  "license": "MIT",
  "languages": ["en", "tr"],
  "ignore": ["venv", "__pycache__", ".git", "secret.txt"]
}
```

#### Required Fields ⚠️
- `API`: Your Google Gemini API key **(REQUIRED)**
- `github_repository`: Your GitHub repository URL **(REQUIRED)**
- `Author`: Your name **(REQUIRED)**

#### Optional Fields 📋
- `project_name`: Defaults to "Unnamed Project"
- `topic`: Defaults to "No topic specified"
- `description`: Defaults to "No description provided"
- `Date`: Can be left empty
- `features`: Array of project features
- `installation`: Array of installation steps
- `usage`: Array of usage examples
- `contribution`: Contribution guidelines
- `license`: License type (affects license file generation)
- `languages`: Languages for README (first is primary)
- `ignore`: Files/folders to ignore during project scan

### 🎯 Usage

#### Method 1: Run All (Recommended)
```bash
python RUN.py
```
This will generate both README.md and LICENSE files simultaneously.

#### Method 2: Individual Scripts
Generate only README:
```bash
python Readme.md-File-Creator.py
```

Generate only LICENSE:
```bash
python License-Creator.py
```

### 📁 Project Structure

```
Readme.md-File-Creator-With-AI-Python/
├── Config.json                    # Configuration file
├── License-Creator.py            # License generation script
├── Readme.md-File-Creator.py     # README generation script
├── RUN.py                        # Main execution script
├── Licenses/                     # License templates directory (comes with defaults)
│   ├── Apache-License-2.0.txt   # Apache 2.0 license template
│   ├── MIT.txt                   # MIT license template
│   ├── GNU-GPLv3.txt           # GNU GPL v3 license template
│   ├── GNU-LGPLv3.txt          # GNU LGPL v3 license template
│   ├── GNU-AGPLv3.txt          # GNU AGPL v3 license template
│   ├── Boost-Software-License-1.0.txt # Boost Software license template
│   ├── Mozilla-Public-License-2.0.txt # Mozilla Public license template
│   └── The-Unlicense.txt         # The Unlicense template
├── README.md                     # Generated README (output)
└── LICENSE                       # Generated LICENSE (output)
```

### 🔧 How It Works

1. **Configuration Reading**: Scripts read your project details from `Config.json`
2. **Project Analysis**: The tool scans your project directory and creates a file tree
3. **AI Generation**: Google Gemini AI generates professional README content based on your project
4. **Multi-Language Support**: Content is translated to specified languages
5. **License Creation**: Appropriate license file is copied from templates
6. **File Output**: README.md and LICENSE files are created in your project root

### 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create your feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### 📋 Supported License Types

The tool comes with pre-installed license templates:
- **MIT License** ✅
- **Apache License 2.0** ✅
- **GNU General Public License v3.0 (GPL-3.0)** ✅
- **GNU Lesser General Public License v3.0 (LGPL-3.0)** ✅
- **GNU Affero General Public License v3.0 (AGPL-3.0)** ✅
- **Boost Software License 1.0** ✅
- **Mozilla Public License 2.0** ✅
- **The Unlicense** ✅

*All license templates are included in the `Licenses/` directory by default.*

### 🚨 Error Handling

The tool includes comprehensive error handling for:
- Missing API key
- Invalid GitHub repository URL
- Missing author information
- Network connectivity issues
- Invalid JSON configuration
- Missing license templates

### 🎨 Customization

You can customize the generated README by:
- Modifying the AI prompts in `Readme.md-File-Creator.py`
- Adding new license templates to the `Licenses/` directory
- Adjusting the ignore list in `Config.json`
- Adding more languages to the `languages` array

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 👨‍💻 Author

**Emrullah Enis Çetinkaya**
- GitHub: [@Software-Guardians](https://github.com/Software-Guardians)
- Project: [Readme.md-File-Creator-With-AI-Python](https://github.com/Software-Guardians/Readme.md-File-Creator-With-AI-Python)

---

## 🌟 TÜRKÇE

### 📖 Açıklama

**AI Destekli README ve Lisans Oluşturucu**, Google Gemini AI kullanarak projeleriniz için otomatik olarak profesyonel README.md ve LICENSE dosyaları oluşturan akıllı bir Python aracıdır. Sadece proje detaylarınızı bir JSON dosyasında yapılandırın ve AI'ın çok dilli destek ile kapsamlı dokümantasyon oluşturmasına izin verin!

### ✨ Özellikler

- 🤖 **AI Üretili İçerik**: Akıllı README oluşturma için Google Gemini 2.5 Flash kullanır
- 🌍 **Çoklu Dil Desteği**: README'yi birden fazla dilde oluşturun (İngilizce, Türkçe ve daha fazlası)
- 📄 **Otomatik Lisans Oluşturma**: MIT, Apache, GPL ve daha fazlası dahil birden fazla lisans türünü destekler
- 🔧 **Akıllı Proje Analizi**: Proje yapısını ve dosyaları otomatik olarak tarar
- ⚙️ **JSON Yapılandırması**: Kolay kullanılabilir yapılandırma sistemi
- 🎨 **Güzel Biçimlendirme**: Emojiler, rozetler ve düzgun yapı ile profesyonel markdown
- 🚫 **Akıllı Filtreleme**: `.git`, `venv`, `__pycache__` gibi yaygın dosyaları otomatik olarak yoksayar
- 🔄 **Tek Tıkla Oluşturma**: Her şeyi tek komutla çalıştırın

### 🚀 Kurulum

#### Önkoşullar
- Python 3.7 veya üzeri
- Google Gemini API anahtarı ([Buradan alın](https://ai.google.dev/))

#### Adımlar
1. **Repository'yi klonlayın:**
   ```bash
   git clone https://github.com/Software-Guardians/Readme.md-File-Creator-With-AI-Python.git
   cd Readme.md-File-Creator-With-AI-Python
   ```

2. **Gerekli paketleri kurun:**
   ```bash
   pip install google-generativeai
   ```

3. **Google Gemini API anahtarınızı alın:**
   - [Google AI Studio](https://ai.google.dev/)'yu ziyaret edin
   - Hesap oluşturun ve API anahtarı oluşturun
   - Yapılandırma için güvenli tutun

### ⚙️ Yapılandırma

`Config.json` dosyasını proje detaylarınızla düzenleyin:

```json
{
  "project_name": "Proje Adınız",
  "github_repository": "https://github.com/kullaniciadi/projeniz",
  "Author": "Tam Adınız",
  "Date": "2024-01-01",
  "topic": "Kısa proje konusu",
  "description": "Detaylı proje açıklaması",
  "API": "gemini-api-anahtariniz-buraya",
  "features": [
    "Özellik 1",
    "Özellik 2",
    "Özellik 3"
  ],
  "installation": [
    "Adım 1: Repository'yi klonlayın",
    "Adım 2: Bağımlılıkları yükleyin",
    "Adım 3: Ayarları yapılandırın"
  ],
  "usage": [
    "Kullanım örneği 1",
    "Kullanım örneği 2"
  ],
  "contribution": "Projeye katkıda bulunma rehberi.",
  "license": "MIT",
  "languages": ["en", "tr"],
  "ignore": ["venv", "__pycache__", ".git", "secret.txt"]
}
```

#### Zorunlu Alanlar ⚠️
- `API`: Google Gemini API anahtarınız **(ZORUNLu)**
- `github_repository`: GitHub repository URL'niz **(ZORUNLU)**
- `Author`: Adınız **(ZORUNLU)**

#### İsteğe Bağlı Alanlar 📋
- `project_name`: Varsayılan "Unnamed Project"
- `topic`: Varsayılan "No topic specified"
- `description`: Varsayılan "No description provided"
- `Date`: Boş bırakılabilir
- `features`: Proje özelliklerinin dizisi
- `installation`: Kurulum adımlarının dizisi
- `usage`: Kullanım örneklerinin dizisi
- `contribution`: Katkı rehberi
- `license`: Lisans türü (lisans dosyası oluşturmayı etkiler)
- `languages`: README dilleri (ilki ana dildir)
- `ignore`: Proje taraması sırasında yoksayılacak dosyalar/klasörler

### 🎯 Kullanım

#### Yöntem 1: Hepsini Çalıştır (Önerilen)
```bash
python RUN.py
```
Bu hem README.md hem de LICENSE dosyalarını aynı anda oluşturacaktır.

#### Yöntem 2: Tekil Scriptler
Sadece README oluştur:
```bash
python Readme.md-File-Creator.py
```

Sadece LICENSE oluştur:
```bash
python License-Creator.py
```

### 📁 Proje Yapısı

```
Readme.md-File-Creator-With-AI-Python/
├── Config.json                    # Yapılandırma dosyası
├── License-Creator.py            # Lisans oluşturma scripti
├── Readme.md-File-Creator.py     # README oluşturma scripti
├── RUN.py                        # Ana çalıştırma scripti
├── Licenses/                     # Lisans şablonları dizini (varsayılan gelir)
│   ├── Apache-License-2.0.txt   # Apache 2.0 lisans şablonu
│   ├── MIT.txt                   # MIT lisans şablonu
│   ├── GNU-GPLv3.txt           # GNU GPL v3 lisans şablonu
│   ├── GNU-LGPLv3.txt          # GNU LGPL v3 lisans şablonu
│   ├── GNU-AGPLv3.txt          # GNU AGPL v3 lisans şablonu
│   ├── Boost-Software-License-1.0.txt # Boost Software lisans şablonu
│   ├── Mozilla-Public-License-2.0.txt # Mozilla Public lisans şablonu
│   └── The-Unlicense.txt         # The Unlicense şablonu
├── README.md                     # Oluşturulan README (çıktı)
└── LICENSE                       # Oluşturulan LICENSE (çıktı)
```

### 🔧 Nasıl Çalışır

1. **Yapılandırma Okuma**: Scriptler proje detaylarınızı `Config.json`'dan okur
2. **Proje Analizi**: Araç proje dizininizi tarar ve dosya ağacı oluşturur
3. **AI Oluşturma**: Google Gemini AI projenize dayalı profesyonel README içeriği oluşturur
4. **Çoklu Dil Desteği**: İçerik belirtilen dillere çevrilir
5. **Lisans Oluşturma**: Uygun lisans dosyası şablonlardan kopyalanır
6. **Dosya Çıktısı**: README.md ve LICENSE dosyları proje kök dizininizde oluşturulur

### 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Nasıl yardım edebileceğiniz:

1. **Repository'yi fork edin**
2. **Feature branch'inizi oluşturun** (`git checkout -b feature/HarikaBirOzellik`)
3. **Değişikliklerinizi commit edin** (`git commit -m 'Harika bir özellik ekle'`)
4. **Branch'e push edin** (`git push origin feature/HarikaBirOzellik`)
5. **Pull Request açın**

### 📋 Desteklenen Lisans Türleri

Araç önceden kurulmuş lisans şablonları ile gelir:
- **MIT License** ✅
- **Apache License 2.0** ✅
- **GNU General Public License v3.0 (GPL-3.0)** ✅
- **GNU Lesser General Public License v3.0 (LGPL-3.0)** ✅
- **GNU Affero General Public License v3.0 (AGPL-3.0)** ✅
- **Boost Software License 1.0** ✅
- **Mozilla Public License 2.0** ✅
- **The Unlicense** ✅

*Tüm lisans şablonları varsayılan olarak `Licenses/` dizininde bulunur.*

### 🚨 Hata Yönetimi

Araç kapsamlı hata yönetimi içerir:
- Eksik API anahtarı
- Geçersiz GitHub repository URL'si
- Eksik yazar bilgisi
- Ağ bağlantısı sorunları
- Geçersiz JSON yapılandırması
- Eksik lisans şablonları

### 🎨 Özelleştirme

Oluşturulan README'yi şu şekillerde özelleştirebilirsiniz:
- `Readme.md-File-Creator.py`'deki AI promptlarını değiştirerek
- `Licenses/` dizinine yeni lisans şablonları ekleyerek
- `Config.json`'daki ignore listesini ayarlayarak
- `languages` dizisine daha fazla dil ekleyerek

### 📄 Lisans

Bu proje MIT License altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

### 👨‍💻 Yazar

**Emrullah Enis Çetinkaya**
- GitHub: [@Software-Guardians](https://github.com/Software-Guardians)
- Proje: [Readme.md-File-Creator-With-AI-Python](https://github.com/Software-Guardians/Readme.md-File-Creator-With-AI-Python)

---

⭐ **Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!**