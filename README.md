# Python Crawler

Python Crawler is a tool for the purpose of collecting vocabulary on VoiceTube.com and make an output file in .csv format for future usage.

## Prerequirement

Manually save the vocabulary page on VoiceTube.com as VoiceTube.html in this folder.

## Installation

```bash
pip install requests bs4 csv
```

## Usage

```python
python crawler.py <fileName>
```

or use default file name if \$1 is empty

```python
python crawler.py
```

### Output

If `crawler.py` has been executed, an updated output.csv will be generated.

## License

[MIT](https://choosealicense.com/licenses/mit/)
