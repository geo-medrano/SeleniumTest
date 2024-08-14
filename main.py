from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import time, argparse

def get_title_web_site(driver: WebDriver, url: str) -> str:
    """Returns the title of a web site

    Args:
        driver (WebDriver): An MS Edge driver
        url (str): The URL's page from getting the title

    Returns:
        str: Title of the web
    """
    driver.get(url)
    return driver.title

# Look for class b_algo, then H2 header //*[@id="b_results"]/li[3]/h2
def search_on_bing(driver: WebDriver, keywords: str) -> list[str] | None:
    url: str = 'https://bing.com'
    driver.get(url)
    element = driver.find_element(By.ID, 'sb_form_q')
    element.send_keys(keywords)
    element.submit()
    search_results = None
    header_list: WebElement = []
    try:
        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'main'))
        )
        result_headers = search_results.find_elements(By.CLASS_NAME, 'b_algo')
        for result in result_headers:
            header_list.append(result.find_element(By.TAG_NAME, 'h2'))
    except:
        print('Error: Not results found')
    else:
        header_list = list(set([header.text for header in header_list if header.text != '']))
        for H2 in header_list:
            print(H2)
    finally:
        return header_list

def main() -> None:
    input_parser = argparse.ArgumentParser(description='Send options to test Selenium')
    input_parser.add_argument('keywords', type=str, help='A list of keywords between doble quotes, e.g., "Selenium tutorial"')
    args = input_parser.parse_args()
    driver = webdriver.Edge()
    search_on_bing(driver, args.keywords)
    driver.quit()

if __name__ == '__main__':
    main()