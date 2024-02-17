# Barebones Whisper (OpenAI) Transcriptions
## Rapid Project Development (RPD)

## Overview
A test project for quick, local audio transcriptions using OpenAI's Whisper. Modify and use it to your preference.

Includes two files: `main.py` (a minimal example) and `main-v2.py` (enhanced with sentence splitting).

## Disclaimer
No APIs or .env variables involved, but as I didn't create the underlying packages, I cannot guarantee data privacy.

Included are test mp3 files to demonstrate functionality.

## Future Considerations
Potential future update: narrator differentiation for enhanced utility.

---

## Getting Started

### Prerequisites
- Python 3.6+
- pip

### Setup and Installation

1. **Clone the repository** to your local machine.

2. **Set up a virtual environment** (optional, but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # On macOS/Linux
   .\env\Scripts\activate   # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
- **For basic transcription**:
  ```bash
  python main.py
  ```
- **For sentence-split transcription**:
  ```bash
  python main-v2.py
  ```

### Deactivating the Virtual Environment
When done, deactivate the virtual environment:
```bash
deactivate
```