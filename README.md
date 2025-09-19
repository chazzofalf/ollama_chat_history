# Ollama Chat History Exporter

A small utility to extract chat histories from an **Ollama** SQLite database, format them as markdown, and convert the result to PDF.  
The project is written by **Cline** (the AI engineer persona) and uses the **gpt‑oss:120b** model for generating explanations and documentation.

## Repository

```
https://github.com/chazzofalf/ollama_chat_history.git
```

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/chazzofalf/ollama_chat_history.git
cd ollama_chat_history

# (optional) create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

## What it does

1. **Extracts** all chat sessions and messages from an Ollama SQLite database (`*.sqlite`).
2. **Generates** a timestamped markdown file (`ollama_chat_history_YYYYMMDD_HHmmSS_mmm.md`) containing the full conversation, grouped by chat ID.
3. **Converts** the markdown to PDF using the bundled `md2pdf` submodule (`md2pdf/md2pdf.py`), which relies on **WeasyPrint**.

## Usage

The project provides two ways to run the exporter:

### Direct Python call

```bash
python generate_ollama_history.py path/to/your_chat.sqlite
```

### Bash wrapper (recommended)

A wrapper script (`generate_ollama_history.sh`) mirrors the behaviour of the original `md2pdf/md2pdf.sh`:

```bash
./generate_ollama_history.sh path/to/your_chat.sqlite
```

The wrapper automatically activates the virtual environment (expected at `./.venv`) before invoking the Python script.

## Files

| File / Directory | Description |
|------------------|-------------|
| `generate_ollama_history.py` | Main Python script that extracts chats and calls the PDF conversion submodule. |
| `generate_ollama_history.sh` | Bash wrapper that activates the virtual environment and runs the Python script. |
| `md2pdf/` | Git submodule containing `md2pdf.py` and a small helper script for markdown‑to‑PDF conversion. |
| `requirements.txt` | Python dependencies: `markdown` and `weasyprint`. |
| `README.md` | This documentation. |

## Dependencies

- **Python 3.9+**
- **markdown** – converts markdown text to HTML (`pip install markdown`).
- **WeasyPrint** – renders HTML to PDF (`pip install weasyprint`).

Both are listed in `requirements.txt`.

## Credits

- **Ollama** – the LLM platform providing the chat database format. <https://ollama.com>
- **Cline** – Visual Studio Code Extension - The collaborative coding agent for complex work. <https://cline.bot>
- **gpt‑oss:120b** – the open‑source GPT model used for generating documentation and assistance. <https://github.com/gpt-oss/120b>

---

Feel free to open issues or pull requests if you encounter any problems or have suggestions for improvement. Happy exporting! 🎉
