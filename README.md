# wallybot

wallybot was used for securing an xbox series x during 11/25 launch for personal use! No Scalping was done :-)
This uses the browser automation API Selenium WebDriver and relies on you to have a Walmart account with your credit card and address info saved.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Selenium 
```bash
pip3 install selenium
```
You also will need to get the latest Mozilla FireFox [geckodriver](https://github.com/mozilla/geckodriver/releases) and put it into your $PATH.

## Usage
Edit the file `config.ini` with your information which is email & password for Walmart account and the CVV of credit card on file.
After that you will have to edit the code to tell what link from config you want to get:

```python
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    driver.get(TEST_URL)                                                                                                                                                                                                               
    driver.maximize_window()
```
So for PS5 you would change TEST_URL to PS5_URL, for xbox series x you would change it to XBOX_URL

## License
[MIT](https://choosealicense.com/licenses/mit/)

