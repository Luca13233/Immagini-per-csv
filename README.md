
# A simple Google Images Link Scraper

I heavily trimmed and modified the code from <https://github.com/ohyicong/Google-Image-Scraper> to take as input a csv file and to output another csv file with all of the extracted links

## How to run

Clone or download the project and [create and activate a python virtual environment](https://docs.python.org/3/library/venv.html)

Inside the project directory:

``` bash
pip install selenium==4.2.0
```

Any later selenium versions will break the code, because  it's using deprecated functions

``` bash
python main.py
```

The program will start pulling data from second column of the file 'input.csv' and appending a link to the output.csv file.
If a link is not found, a newline character will be printed and the program will continue execution.

## [ERROR] Couln't extract valid link

If you encounter this error a lot try increasing `load_time` (in seconds) in main.py, it will increase the time given to the page (and image links) to load but it will make code execution slower

## Selenium doesn't work / Program doesn't start

Try either removing `options.add_argument("--remote-debugging-port=9222");` in Scraper.py or changing the port number (Google is your friend)
This program was tested on Ubuntu 20.04.5 LTS and python 3.8.10

## Sample output

``` log
[INFO] Started chromium browser
[INFO] Set window size
[INFO] Visited google.com
[INFO] Loop number 0
[INFO] Gathering image links
[INFO] Clicked on image successfully
 [INFO] FLASH DRIVE USB2.0 16GB Silicon Power Touch825 Silver    https://i.ebayimg.com/images/g/AqUAAOSwZQxW6av~/s-l500.jpg
[INFO] Google search ended
--- 2.50 seconds ---
[INFO] Loop number 1
[INFO] Gathering image links
[INFO] Clicked on image successfully
 [INFO] FLASH DRIVE USB2.0 32GB Silicon Power UltimaII Nero      https://www.distrelec.it/Web/WebShopImages/landscape_large/82/48/SiliconPower_Ultima_II-_I_02_32GB.jpg
[INFO] Google search ended
--- 1.92 seconds ---
[INFO] Loop number 2
[INFO] Gathering image links
[INFO] Clicked on image successfully
[ERROR] Couln't extract valid link
[ERROR] Couln't extract valid link
[INFO] Google search ended
--- 1.88 seconds ---
```
