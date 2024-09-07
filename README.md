# Fixed Width File Parser

## Description
This Python project parses a fixed-width file and generates a CSV file using a specification that defines the width of each field

## How to Run
1. Clone the repo.
2. Build Docker image: `docker build -t fixed-width-parser .`
3. Run the parser: `docker run fixed-width-parser`

## Input/Output
- Input: `fixed_width_file.txt` (Fixed width)
- Output: `output.csv` (CSV)

## Test
Run tests using:
```bash
python -m unittest tests/test_parser.py
