# hermes-quicknotes

Lightweight CLI tool untuk manage notes dari terminal. Simple, fast, dan no dependencies.

## Features

- ✅ Add notes dengan title & content
- ✅ List semua notes dengan preview
- ✅ Show detail note lengkap
- ✅ Delete notes
- ✅ Search notes by title atau content
- ✅ Auto-save ke `~/.quicknotes/notes.json`

## Installation

```bash
git clone https://github.com/Fizh41/hermes-quicknotes.git
cd hermes-quicknotes
chmod +x quicknotes.py
sudo ln -s $(pwd)/quicknotes.py /usr/local/bin/quicknotes
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

### Show a specific note
```bash
quicknotes show "Project Ideas"
```

### Search notes
```bash
quicknotes search "agent"
```

### Delete a note
```bash
quicknotes delete "Project Ideas"
```

## Storage

Notes disimpan di `~/.quicknotes/notes.json` dalam format JSON:

```json
{
  "Project Ideas": {
    "content": "Build AI agent...",
    "created": "2026-05-23T12:00:00",
    "updated": "2026-05-23T12:00:00"
  }
}
```

## Requirements

- Python 3.7+
- No external dependencies

## License

MIT
