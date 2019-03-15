# Once in a π

Find any unicode string in π. Honoring [pi day](https://en.wikipedia.org/wiki/Pi_Day)

A small python script that transforms a `unicode` string to numbers - using `ord()` - and tries to find that string of
number in an approximation of π.


```bash
usage: once_in_a.py [-h] [--pi PI] [--to TO] lookup_string [lookup_string ...]

Find a random unicode string in an aproximation of PI

positional arguments:
  lookup_string  The unicode string you want to find

optional arguments:
  -h, --help     show this help message and exit
  --pi PI        Set your prefered approximation of π (default: 355/113)
  --to TO        Path to the file to write the results to.
 ```

**NOTA BENE:** the longer the string the longer the program will run, e.g. `test` is `116101115116` which is not a common pattern in π. For longer strings I suggest you use the flag `--to` and [orphan](https://en.wikipedia.org/wiki/Orphan_process) the process.

## Use

Make sure to have [Python 3](https://www.python.org/downloads/) installed.

1. Get the code
  ```bash
  # Clone the repository
  git clone https://github.com/dasdachs/once-in-a-pi
  ```
  or 
  ```bash
  curl https://raw.githubusercontent.com/dasdachs/once-in-a-pi/master/once_in_a.py > once_in_a.py
2. Run the code
  ```bash
  python3 once_in_a.py [lookup] # POSIX
  python once_in_a.py [lookup]  # Windows
  ```
