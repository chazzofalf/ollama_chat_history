#!/usr/bin/env python3
"""
Generate a comprehensive markdown export of the Ollama chat history stored in
`db_20250919_091726_ollama.sqlite` and convert it to PDF using the
`md2pdf.sh` script located at `${HOME}/.local/bin/md2pdf.sh`.

The markdown file is named:
    ollama_chat_history_YYYYMMDD_HHmmSS_mmm.md
where:
    YYYY – year
    MM   – month
    DD   – day
    HH   – hour (24‑hour clock)
    mm   – minute
    SS   – second
    mmm  – millisecond
"""

import os
import sqlite3
import subprocess
from datetime import datetime

def fetch_chat_history(db_path: str):
    """Return a dict mapping chat_id to a list of (role, content) tuples."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # Retrieve all messages ordered by chat and timestamp
    cur.execute(
        "SELECT chat_id, role, content FROM messages ORDER BY chat_id, created_at"
    )
    rows = cur.fetchall()
    conn.close()

    chats = {}
    for chat_id, role, content in rows:
        chats.setdefault(chat_id, []).append((role, content))
    return chats

def format_markdown(chats: dict) -> str:
    """Create a markdown representation of the chats."""
    lines = ["# Ollama Chat History", ""]
    for chat_id, messages in chats.items():
        lines.append(f"## Chat ID: `{chat_id}`")
        lines.append("")
        for role, content in messages:
            # Capitalize role for readability
            role_cap = role.capitalize()
            # Escape backticks in content to avoid markdown issues
            safe_content = content.replace("`", "`\u200b")
            lines.append(f"**{role_cap}:**")
            lines.append("")
            lines.append(f"{safe_content}")
            lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)

def main():
    # Paths
    import sys
    if len(sys.argv) > 1:
        db_path = sys.argv[1]
    else:
        raise ValueError("Database path argument required. Provide the Ollama SQLite file as the first command-line argument.")
    if not os.path.isfile(db_path):
        raise FileNotFoundError(f"Database not found at {db_path}")

    # Fetch and format data
    chats = fetch_chat_history(db_path)
    markdown = format_markdown(chats)

    # Build timestamp with milliseconds
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S_%f")[: -3]  # trim to milliseconds
    md_filename = f"ollama_chat_history_{timestamp}.md"

    # Write markdown file
    with open(md_filename, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Markdown file written: {md_filename}")

    # Convert to PDF using the md2pdf submodule script
    md2pdf_script = os.path.join(os.path.dirname(__file__), "md2pdf", "md2pdf.py")
    if not os.path.isfile(md2pdf_script):
        raise FileNotFoundError(f"md2pdf script not found at {md2pdf_script}")

    # Call the submodule script using the current Python interpreter
    try:
        subprocess.run([sys.executable, md2pdf_script, md_filename], check=True)
        print(f"PDF conversion completed for {md_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error during PDF conversion: {e}")

if __name__ == "__main__":
    main()
