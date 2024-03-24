from selenium import webdriver
import time

def change_proxy(driver, proxy):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(options=options)

def open_website(url, num_tabs, proxy_list):
    driver = webdriver.Chrome()
    current_proxy_index = 0
    change_interval = 5 

    try:
        for i in range(int(num_tabs)):
            
            if i > 0 and i % change_interval == 0:
                current_proxy_index = (current_proxy_index + 1) % len(proxy_list)
                change_proxy(driver, proxy_list[current_proxy_index])
                print(f"Changed proxy to: {proxy_list[current_proxy_index]}")
                time.sleep(1) 

            driver.execute_script("window.open('" + url + "');")
            time.sleep(0.5)

        driver.switch_to.window(driver.window_handles[0])

    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

website_url = input("Enter the URL: ")
num_tabs = input("How many tabs do you want: ")

proxy_list = [
    "180.254.239.207:8080",
    "180.254.239.207:8080",
    "94.158.165.165:80"
]

open_website(website_url, num_tabs, proxy_list)
