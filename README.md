# Päevapakkumised Scraper

## Requirements

- Python 3.11+
- pip
- venv
- `requests` and `beautifulsoup4` Python packages

## Setup

1. Create a virtual environment and activate:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run

   ```bash
   python pakkumised.py
   ```

## Usage

The places and the asian places are read from the .json files in this project.
These should be present in the root directory of the project.
These can be modified by your preference.

The order of the in the .json file corresponds to the order of the output.

### Running

  ```bash
  python pakkumised.py             # Show all offers
  python pakkumised.py --no-asian  # Exclude Asian restaurants
  ```

