import os
import time
import subprocess
import logging
import json
import shutil
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO)

# VARIABLES #
browser_port = 8989
file_folder = ''  # path for media files for upload: webp
uploaded_folder = ''  # path for uploaded media files
json_folder = ''  # path for metadata files: json


put_on_market = "Yes"
token_price = 0.016  # set price here
collection = "Tiny Cafe"  # choose your smart contract (Collection) name
loop_title = "#"  # set title name here
image_file_format = "webp"  # choose format for upload file "png" , "jpg" , "mp4" or "webp"
cover_file_format = "jpg"  # choose format for cover file "png" , "jpg" , "mp4"
cover_name = "r_0001"
token_description = ""  # write description for all items here
royalties = "10"


# XPATH and CSS #
CREATE_SINGLE_BUTTON = "button[id='create-single']"
DRAFT_DISCARD_BUTTON = "button[data-marker='restore-modal/discardButton']"
ADD_ATTACHMENT_BUTTON = "//*[@id='root']/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/div/input"
ADD_COVER_BUTTON = '//*[@id="root"]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div/div[2]/div/div/div/button'
FIXED_PRICE_BUTTON = "img[alt='Fixed price']"
PRICE_INPUT_FIELD = "input[data-marker='root/appPage/create/form/price/input/priceInput']"
PUT_ON_MARKET_SWITCHER = "//*[@id='root']/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div/div[2]/button/div/div"
TINY_CAFE_COLLECTION_BUTTON = "button[data-marker='root/appPage/create/form/collectionSelector/collectionButton/Tiny Cafe']"
RARIBLE_COLLECTION_BUTTON = "button[data-marker='root/appPage/create/form/collectionSelector/collectionButton/Rarible']"
NAME_INPUT = "input[data-marker='root/appPage/create/form/nameInput']"
DESCRIPTION_INPUT = "textarea[testid='root/appPage/create/form/descriptionInput']"
ROYALTIES_INPUT = "input[data-marker='root/appPage/create/form/royaltiesInput']"
ADVANCED_SETTING_BUTTON = '//*[@id="root"]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[12]/div/button'
MINT_BUTTON = "button[data-marker='root/appPage/create/form/createButton']"
TRY_AGAIN_BUTTON = "//button[normalize-space()='Try again']"
SCROLLED_BUTTON = '//*[@id="app-content"]/div/div[2]/div/div[3]/div[1]'
MINT_ANOTHER_BUTTON = "button[data-marker='mint-modal/finish/mintAnotherButton']"


def open_chrome_profile():
    subprocess.Popen(['start', 'chrome', '--remote-debugging-port={port_num}'.format(port_num=browser_port),
                      '--user-data-dir=' + main_directory + '/chrome_profile'], shell=True)


def click_element(code, search_type=By.CSS_SELECTOR, fail_message="Element not found"):
    while True:
        try:
            ce = wait.until(ec.presence_of_element_located((search_type, code)))
            ce.click()
            if code == MINT_BUTTON or code == SCROLLED_BUTTON:
                time.sleep(2)
            else:
                time.sleep(1)
            break
        except:
            logging.warning(fail_message + ": " + code + "\nretrying...")
            time.sleep(1)


def send_keys_element(code, key, search_type=By.CSS_SELECTOR, fail_message="Element not found"):
    while True:
        try:
            ske = wait.until(ec.presence_of_element_located((search_type, code)))
            if code == ADD_ATTACHMENT_BUTTON or code == ADD_COVER_BUTTON:
                ske.send_keys(key)
            else:
                ske.clear()
                ske.send_keys(key)
            time.sleep(1)
            break
        except:
            logging.warning(fail_message + ": " + code + "\nretrying...")
            time.sleep(1)


def go_to(address, fail_message="Address not found"):
    while True:
        try:
            driver.get(address)
            break
        except:
            logging.warning(fail_message + ": " + address + "\nretrying...")
            time.sleep(1)


def fill_all_properties(json_name):  # get metadata from file and insert into metadata fields
    prop_key = 1
    prop_value = 2

    with open(f'{json_folder}{json_name}.json') as meta:
        meta = json.load(meta)
        for nft_property in meta:
            for key in nft_property:
                prop_key_field = f'//*[@id="root"]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[12]/div/div[1]/div[2]/div[{prop_key}]/div/div/input'
                prop_value_field = f'//*[@id="root"]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[12]/div/div[1]/div[2]/div[{prop_value}]/div/div/input'
                send_keys_element(prop_key_field, key, By.XPATH)
                prop_key += 2
                send_keys_element(prop_value_field, nft_property[key], By.XPATH)
                prop_value += 2


def click_metamask_sign_button():
    while True:
        while True:
            try:
                t = driver.find_element(By.XPATH, TRY_AGAIN_BUTTON)
                driver.execute_script("arguments[0].click();", t)
                logging.info("Try again 1 found and clicked.")
            except Exception:
                logging.info("Try again 1 not found, skipping.")
                break
        try:
            logging.info("Waiting for metamask popup, please wait...")
            time.sleep(2)
            for handle in driver.window_handles:
                if handle != main_page:
                    login_page = handle
            driver.switch_to.window(login_page)
            break
        except Exception:
            logging.info("Metamask popup not found. There might be a 'second try again', retrying...")
            try:
                logging.info("checking if there is a second try")
                tr = driver.find_element(By.XPATH, TRY_AGAIN_BUTTON)
                driver.execute_script("arguments[0].click();", tr)
                logging.info("Try again 2 found and clicked.")
            except Exception:
                logging.info("Try again 2 not found, skipping.")
    try:
        click_element(SCROLLED_BUTTON, By.XPATH)
        logging.info("Scrolled down and clicked")
    except Exception:
        logging.warning("Not scrolled down and clicked")
        pass


# execution steps
main_directory = os.getcwd()
open_chrome_profile()
op = webdriver.ChromeOptions()
op.add_experimental_option("debuggerAddress", "localhost:{port_num}".format(port_num=browser_port))
driver = webdriver.Chrome(options=op, service=Service(ChromeDriverManager().install()))
main_page = driver.current_window_handle
wait = WebDriverWait(driver, 10)
logging.info("Connected to browser on port {port_num}".format(port_num=browser_port))
# driver.set_window_size(360, 840)
driver.switch_to.window(driver.window_handles[0])
logging.info("Window names ", driver.window_handles)
go_to("https://rarible.com/create/start/ethereum")
click_element(CREATE_SINGLE_BUTTON)

items = os.listdir(file_folder)
random.shuffle(items)
item_count = len(items)

for item in items:
    image_name = item.split('.')[0]
    image_path = os.path.abspath(f'{file_folder}{image_name}.{image_file_format}')
    # cover_path = os.path.abspath(f'{file_folder}{cover_name}.{cover_file_format}')

    logging.info(f"Uploading: {image_name} - {item_count} to go...")

    # discard image if draft opens
    while True:
        try:
            logging.info("Checking for draft discard button, please wait...")
            wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, DRAFT_DISCARD_BUTTON))).click()
            break
        except Exception:
            break

    send_keys_element(ADD_ATTACHMENT_BUTTON, image_path, By.XPATH)  # attach new vid
    # send_keys_element(ADD_COVER_BUTTON, cover_path, By.XPATH)  # attach new cover
    click_element(FIXED_PRICE_BUTTON)  # choose Fixed Price

    if put_on_market == "No":
        click_element(PUT_ON_MARKET_SWITCHER, By.XPATH, "Warning: NFT put on market")  # inform that lazy mint off
        ADVANCED_SETTING_BUTTON = '//*[@id="root"]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[10]/div/button'
    else:
        send_keys_element(PRICE_INPUT_FIELD, token_price)  # set price

    if collection == "Tiny Cafe":
        click_element(TINY_CAFE_COLLECTION_BUTTON)  # choose your own collection
    else:
        click_element(RARIBLE_COLLECTION_BUTTON)  # choose default collection

    send_keys_element(NAME_INPUT, loop_title + str(image_name))  # set name for token
    send_keys_element(DESCRIPTION_INPUT, token_description)  # set token description
    send_keys_element(ROYALTIES_INPUT, royalties)  # set percent of royalties
    click_element(ADVANCED_SETTING_BUTTON, By.XPATH)  # open advanced settings to fill properties
    fill_all_properties(image_name)
    click_element(MINT_BUTTON)  # start minting

    click_metamask_sign_button()  # don't know exactly what happens
    click_element("button[class='button btn--rounded btn-primary']")  # sign signature request
    driver.switch_to.window(main_page)  # to focus on firstly opened window

    click_metamask_sign_button()  # don't know exactly what happens
    click_element("button[class='button btn--rounded btn-primary']")  # sign signature request
    driver.switch_to.window(main_page)  # to focus on firstly opened window

    # store items in case of fail
    with open('/database/uploaded.txt', 'a', encoding='UTF-8') as uploaded_items:
        uploaded_items.write(str(image_name) + '\n')
    shutil.move(f'{file_folder}{image_name}.{image_file_format}', uploaded_folder)
    click_element(MINT_ANOTHER_BUTTON)  # to get into the loop and prepare another NFT
    driver.switch_to.window(main_page)  # to focus on firstly opened window

    item_count = item_count - 1
