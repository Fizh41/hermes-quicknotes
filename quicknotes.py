#!/usr/bin/env python3
"""hermes-quicknotes - Lightweight CLI note manager."""

import sys
import os
import json
from datetime import datetime
from pathlib import Path

NOTES_DIR = Path.home() / ".quicknotes"
NOTES_FILE = NOTES_DIR / "notes.json"

def init():
    """Initialize notes directory."""
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    if not NOTES_FILE.exists():
        save_notes({})

def load_notes() -> dict:
    """Load notes from file."""
    init()
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_notes(notes: dict):
    """Save notes to file."""
    init()
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(title: str, content: str):
    """Add a new note."""
    notes = load_notes()
    notes[title] = {
        "content": content,
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat()
    }
    save_notes(notes)
    print(f"✅ Note added: {title}")

def list_notes():
    """List all notes."""
    notes = load_notes()
    if not notes:
        print("📝 No notes yet. Use: quicknotes add <title> <content>")
        return
    
    print(f"📝 {len(notes)} notes:\n")
    for title, data in notes.items():
        updated = data["updated"][:10]
        preview = data["content"][:60] + "..." if len(data["content"]) > 60 else data["content"]
        print(f"  {title} ({updated})")
        print(f"    {preview}\n")

def show_note(title: str):
    """Show a specific note."""
    notes = load_notes()
    if title not in notes:
        print(f"❌ Note not found: {title}")
        return
    
    note = notes[title]
    print(f"📝 {title}")
    print(f"   Created: {note['created'][:19]}")
    print(f"   Updated: {note['updated'][:19]}")
    print(f"\n{note['content']}")

def delete_note(title: str):
    """Delete a note."""
    notes = load_notes()
    if title not in notes:
        print(f"❌ Note not found: {title}")
        return
    
    del notes[title]
    save_notes(notes)
    print(f"🗑️ Deleted: {title}")

def search_notes(query: str):
    """Search notes by content."""
    notes = load_notes()
    results = []
    for title, data in notes.items():
        if query.lower() in title.lower() or query.lower() in data["content"].lower():
            results.append(title)
    
    if results:
        print(f"🔍 Found {len(results)} matches:")
        for title in results:
            print(f"  • {title}")
    else:
        print(f"🔍 No matches for: {query}")

def main():
    if len(sys.argv) < 2:
        print("quicknotes - Lightweight CLI note manager")
        print("\nUsage:")
        print("  quicknotes add <title> <content>   Add a note")
        print("  quicknotes list                     List all notes")
        print("  quicknotes show <title>             Show a note")
        print("  quicknotes delete <title>           Delete a note")
        print("  quicknotes search <query>           Search notes")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "add":
        if len(sys.argv) < 4:
            print("Usage: quicknotes add <title> <content>")
            return
        add_note(sys.argv[2], " ".join(sys.argv[3:]))
    elif cmd == "list":
        list_notes()
    elif cmd == "show":
        if len(sys.argv) < 3:
            print("Usage: quicknotes show <title>")
            return
        show_note(sys.argv[2])
    elif cmd == "delete":
        if len(sys.argv) < 3:
            print("Usage: quicknotes delete <title>")
            return
        delete_note(sys.argv[2])
    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Usage: quicknotes search <query>")
            return
        search_notes(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
