#!/bin/bash
gnome-terminal -- bash -c "source ~/Desktop/vscode/myenv/bin/activate && uvicorn api.main:app --reload; exec bash"

gnome-terminal -- bash -c "source ~/Desktop/vscode/myenv/bin/activate && streamlit run src/frontend.py; exec bash"