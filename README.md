# Capt. Cruncher
Capt. Cruncher is a Python script for generating custom wordlists. \
This has purely been created for use with CTF's.

![Screenshot 2023-06-09 150542](https://github.com/B0neShAd0w/Capt-Cruncher/assets/117080369/976e8506-02f0-41d7-abda-6993b6cdc04e)

## Setup

#### Clone the repository
```shell
git clone https://github.com/B0neShad0w/Capt-Cruncher
cd Capt-Cruncher
```

#### Install requirements
```shell
pip install -r requirements.txt
```

## Usage

#### Import NMEA data from file and export to an KML file.

```python
# This command will create a default output file called wordlist.txt using all permutations of the input words
python Capt-Cruncher.py --input apple pear orange

# This command will create an output file called dictionary.txt using all permutations of the input words
python Capt-Cruncher.py --input apple pear orange --output dictionary.txt

# This command will add a specified separator between each of the input words
python Capt-Cruncher.py --input apple pear orange --separator _

# This command will append the specified to each result
python Capt-Cruncher.py --input apple pear orange --append 123

# This command will prefix each result with the specified
python Capt-Cruncher.py --input apple pear orange --prefix abc

# This command will prefix, append, and add the specified separator to each result and output to a file called my_wordlist.txt
python Capt-Cruncher.py --input apple pear orange --prefix abc --append 123! --separator - --output my_wordlist.txt
```

## Planned features

- [X] None currently

## Contact
Feel free to contact me on <a href="https://twitter.com/B0neShad0w">Twitter</a>
