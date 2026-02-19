# Data Directory

This directory is for storing your collected data files.

## Guidelines

- Organize data by type or date
- Use descriptive filenames
- Document data sources and collection methods
- Keep raw data separate from processed data

## File Formats

Supported data formats include:
- CSV files (`.csv`)
- Excel files (`.xlsx`, `.xls`)
- JSON files (`.json`)
- SQLite databases (`.db`, `.sqlite`)

## Note

Large data files are ignored by git (see `.gitignore`). Consider using Git LFS for large datasets if needed.

## Example Structure

```
data/
├── raw/           # Raw, unprocessed data
├── processed/     # Cleaned and processed data
└── external/      # Data from external sources
```
