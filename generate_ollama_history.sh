#!/usr/bin/env bash
# Wrapper script to activate the project's virtual environment and run generate_ollama_history.py
# Works regardless of the current working directory from which the script is invoked.

# Resolve the directory where this script resides, following symlinks
SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
SCRIPT_DIR="$(cd "$(dirname "$SCRIPT_PATH")" && pwd)"

# Path to the virtual environment (assumed to be located in the same directory as this script)
VENV_DIR="${SCRIPT_DIR}/.venv"

# Ensure the virtual environment exists
if [ ! -d "${VENV_DIR}" ]; then
  echo "Error: Virtual environment not found at ${VENV_DIR}"
  exit 1
fi

# Activate the virtual environment
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

# Execute the Python script with any passed arguments
python "${SCRIPT_DIR}/generate_ollama_history.py" "$@"
