# pyrandnpc
Generates random NPCs for tabletop RPGs

## Dependencies
1. Install python
2. `pip install -r requirements.txt`

## Traits
Possible traits are stored in text files ie. `bonds.txt` will list all bonds. To add new entries, put a possible trait for the given category on a new line within the file.

## Races and Names
The `races.txt` file is filled with possible races. Each line is a comma separated list of & `race, first_names_filename.txt, last_names_filename.txt`

The text files containing first and last names follow the same pattern as the possible traits files: a different name on each line.

## Use
To use, simply run main.py

`python main.py`

The generated characters are stored in 'characters.xlsx'