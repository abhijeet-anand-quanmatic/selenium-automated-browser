import time
import random
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from faker import Faker
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Faker for dummy data generation
fake = Faker()

# Operating Systems
OS_TYPES = ["android", "mac", "windows", "ios"]

# Browsers mapped to OS
BROWSER_OS_MAPPING = {
    "android": ["chrome"],
    "mac": ["chrome", "safari", "firefox", "edge"],
    "windows": ["chrome", "firefox", "edge"],
    "ios": ["safari"],
}

# User agents for different devices and OS
USER_AGENTS = {
    "android": [
        "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; Tablet) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0 Mobile Safari/537.36",
    ],
    "mac": [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0 Safari/537.36",
    ],
    "windows": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0 Safari/537.36",
    ],
    "ios": [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 13_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0 Safari/537.36",
    ],
}

# List of proxy servers (Replace with valid proxies)
PROXIES = [
    "103.250.166.12:6666",  # India
    "185.199.229.156:7492",  # Germany
    "91.217.42.3:8080",  # France
]


# Function to start the Selenium driver
def start_driver(selected_os):
    options = Options()

    # Random user-agent based on OS
    user_agent = random.choice(USER_AGENTS[selected_os])
    options.add_argument(f"user-agent={user_agent}")

    # Choose a random proxy
    proxy = random.choice(PROXIES)
    options.add_argument(f"--proxy-server={proxy}")

    # Enable headless mode for GitHub Actions
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Start WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    return driver, proxy  # ✅ Return both driver and selected proxy


# Function to collect dummy data
def collect_dummy_data(driver, url, session_duration, proxy):
    driver.get(url)
    start_time = time.time()

    print(f"📜 Browsing {url} for {session_duration} seconds...")

    while time.time() - start_time < session_duration:
        scroll_amount = random.randint(300, 600)
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(random.uniform(2, 5))

        # Click on a random link if available
        links = driver.find_elements(By.TAG_NAME, "a")
        if links and time.time() - start_time > session_duration / 2:
            link = random.choice(links)
            link_text = link.text.strip() or link.get_attribute("href")
            print(f"🔗 Clicking on: {link_text}")
            link.click()
            time.sleep(3)
            break  # Stop scrolling after clicking a link

    # Generate fake user data
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "phone": fake.phone_number(),
        "user_agent": driver.execute_script("return navigator.userAgent;"),
        "proxy": proxy,  # ✅ Now correctly assigned
    }
    return data


# Main execution loop
if __name__ == "__main__":
    collected_data = []
    url = "https://quanmatic.com/"

    for _ in range(random.randint(6, 10)):
        selected_os = random.choice(OS_TYPES)  # Pick a random OS
        session_duration = random.randint(10, 50)  # Random session duration

        print(f"\n🚀 Starting session on {selected_os.upper()} | Duration: {session_duration}s")
        driver, proxy = start_driver(selected_os)  # ✅ Get proxy from start_driver()

        try:
            dummy_data = collect_dummy_data(driver, url, session_duration, proxy)  # ✅ Pass proxy
            collected_data.append(dummy_data)
            print("✅ Data collected:", dummy_data)
        except Exception as e:
            print("⚠️ Error collecting data:", e)
        finally:
            print(f"\n❌ Closing session after {session_duration}s...\n")
            driver.quit()
            time.sleep(5)
