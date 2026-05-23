# hermes-quicknotes

A lightweight Python CLI tool for managing notes directly from the terminal. Supports add, list, show, delete, and search commands with auto-save to JSON. Zero dependencies, just pure Python 3. Perfect for developers, sysadmins, and anyone who lives in the terminal.

## Why hermes-quicknotes?

- **Zero Dependencies** — Pure Python 3, no external packages needed
- **Fast & Lightweight** — Minimal memory footprint, instant startup
- **Terminal Native** — Designed for developers who live in the CLI
- **Simple JSON Storage** — Notes stored in `~/.quicknotes/notes.json`, easy to backup/sync
- **Search Capability** — Find notes by title or content instantly
- **Timestamps** — Auto-track creation and update times for each note

## Features

- ✅ **Add notes** with title and content
- ✅ **List all notes** with preview (first 60 chars)
- ✅ **Show full note** with timestamps
- ✅ **Delete notes** by title
- ✅ **Search notes** by title or content
- ✅ **Auto-save** to `~/.quicknotes/notes.json`
- ✅ **JSON format** — human-readable, easy to parse

## Installation

### Option 1: Clone & Link (Recommended)
```bash
git clone https://github.com/Fizh41/hermes-quicknotes.git
cd hermes-quicknotes
chmod +x quicknotes.py
sudo ln -s $(pwd)/quicknotes.py /usr/local/bin/quicknotes
```

### Option 2: Copy to PATH
```bash
git clone https://github.com/Fizh41/hermes-quicknotes.git
sudo cp hermes-quicknotes/quicknotes.py /usr/local/bin/quicknotes
sudo chmod +x /usr/local/bin/quicknotes
```

## Usage

### Add a note
```bash
quicknotes add "Project Ideas" "Build AI agent for automation, integrate with 9Router"
```

### List all notes
```bash
quicknotes list
```

Output:
```
📝 2 notes:

  Project Ideas (2026-05-23)
    Build AI agent for automation, integrate with 9Router...

  Meeting Notes (2026-05-22)
    Discussed deployment strategy for Hermes Agent...
```

### Show a specific note
```bash
quicknotes show "Project Ideas"
```

Output:
```
📝 Project Ideas
   Created: 2026-05-23 12:00:00
   Updated: 2026-05-23 12:00:00

Build AI agent for automation, integrate with 9Router
```

### Search notes
```bash
quicknotes search "agent"
```

Output:
```
🔍 Found 2 matches:
  • Project Ideas
  • Agent Architecture Notes
```

### Delete a note
```bash
quicknotes delete "Project Ideas"
```

Output:
```
🗑️ Deleted: Project Ideas
```

## Storage

Notes are stored in `~/.quicknotes/notes.json` in JSON format:

```json
{
  "Project Ideas": {
    "content": "Build AI agent for automation, integrate with 9Router",
    "created": "2026-05-23T12:00:00",
    "updated": "2026-05-23T12:00:00"
  },
  "Meeting Notes": {
    "content": "Discussed deployment strategy for Hermes Agent",
    "created": "2026-05-22T10:30:00",
    "updated": "2026-05-22T10:30:00"
  }
}
```

This makes it easy to:
- Backup notes to cloud storage (Dropbox, Google Drive, etc.)
- Sync across machines
- Parse programmatically
- Version control with git

## Requirements

- Python 3.7 or higher
- No external dependencies

## Project Stats

- **Lines of Code:** 134 (main script)
- **Dependencies:** 0 (zero external packages)
- **File Size:** ~3.8 KB
- **License:** MIT

## Use Cases

### For Developers
- Quick capture of code snippets and ideas
- Store API endpoints and credentials (locally, securely)
- Track debugging notes and solutions

### For Sysadmins
- Log server maintenance tasks
- Store command references
- Track deployment notes

### For Anyone
- Daily task lists
- Project brainstorming
- Quick reference material
- Learning notes

## Examples

### Capture a quick idea
```bash
quicknotes add "Hermes Agent Feature" "Add support for multi-chain wallet operations with automatic gas optimization"
```

### Store a useful command
```bash
quicknotes add "Docker Cleanup" "docker system prune -a --volumes"
```

### Keep meeting notes
```bash
quicknotes add "Team Standup 2026-05-23" "Discussed Q2 roadmap, prioritized NFT minting automation, assigned tasks"
```

### Search for related notes
```bash
quicknotes search "docker"
```

## Roadmap

Potential future features:
- [ ] Tags/categories for notes
- [ ] Export to Markdown/PDF
- [ ] Sync with cloud storage
- [ ] Note encryption
- [ ] Web UI (optional)

## Contributing

Feel free to fork, modify, and submit PRs. This is intentionally kept simple and lightweight.

## License

MIT License — See LICENSE file for details

## Author

Created by [Fizh41](https://github.com/Fizh41)

---

**Made with ❤️ for terminal enthusiasts**
