# Flashy - Korean Flashcard App

A Tkinter-based flashcard application for learning Korean words with English translations.

## Features
- Displays Korean words with automatic flip to English translation after 3 seconds
- Tracks known words by removing them from the deck
- Saves progress to a CSV file
- Visual feedback with right/wrong buttons
- Congratulatory message when all words are learned

## Prerequisites
- Python 3.x
- Required Python packages:
  - `tkinter` (usually included with Python)
  - `pandas`
- Required assets:
  - `images/card_front.png` (800x526 pixels)
  - `images/card_back.png` (800x526 pixels)
  - `images/right.png` (button image)
  - `images/wrong.png` (button image)
- Data files:
  - `data/korean 100 words.csv` (initial word list)
  - `data/words_to_learn.csv` (generated progress file)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/flashy-korean.git
cd flashy-korean
```

2. Install dependencies:
```bash
pip install pandas
```

3. Ensure all image files and initial CSV are in the correct directories

## Usage
1. Run the application:
```bash
python flashy.py
```

2. Use the GUI:
- Click the wrong button (✗) to see next card
- Click the right button (✓) to mark word as known
- Card flips automatically after 3 seconds

## How It Works
- Loads words from `korean 100 words.csv` initially
- Uses `words_to_learn.csv` for subsequent runs
- Shows Korean word first, flips to English after 3 seconds
- Right button removes word from deck and saves progress
- Wrong button shows next card
- Ends with congratulatory message when deck is empty

## File Structure
- `flashy.py`: Main application file
- `data/`
  - `korean 100 words.csv`: Initial word list
  - `words_to_learn.csv`: Progress tracking (auto-generated)
- `images/`
  - `card_front.png`: Front card background
  - `card_back.png`: Back card background
  - `right.png`: Right button image
  - `wrong.png`: Wrong button image

## Data Format
CSV files contain:
- `Korean`: Korean word column
- `English`: English translation column

## GUI Components
- Canvas with card (800x526)
- Language label (Korean/English)
- Word text
- Right (✓) and Wrong (✗) buttons

## Customization
- `BACKGROUND_COLOR`: Default "#B1DDC6"
- Flip time: 3000ms (3 seconds) in `window.after()`
- Font sizes and styles in canvas text
- Initial CSV file path/name

## Notes
- Creates `words_to_learn.csv` if not present
- Progress persists between sessions
- Background color matches card edges
- Requires all image assets to function
- Prints data dictionary to console for debugging

## Requirements.txt
```
pandas
```

## Limitations
- No manual word addition
- Basic error handling (FileNotFoundError only)
- Fixed 3-second flip time
- Single language pair (Korean-English)

## License
[MIT License](LICENSE)

## Disclaimer
- Ensure all image and CSV files are present
- CSV must have "Korean" and "English" columns
- Designed for 100-word initial dataset
- Progress resets if initial CSV is modified
```

