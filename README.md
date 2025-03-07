

# 🚀 Selenium Automated Browser Bot

## 📌 Overview
This **Selenium bot** automates web browsing by:
- Randomly selecting **OS, browser, and proxy**
- Browsing **Quanmatic.com** (or any website)
- Scrolling and clicking links **like a real user**
- Running in **stealth mode** with **headless browsing**
- Logging **user-agent, IP address, and session details**

This bot is fully automated using **GitHub Actions**, running **every hour**.

---

## 🛠 Features
✅ **Rotates OS** (Android, macOS, Windows, iOS)  
✅ **Switches Browsers** (Chrome, Firefox, Safari, Edge)  
✅ **Uses Proxies** for **location spoofing**  
✅ **Stealth Mode** (Undetectable headless browsing)  
✅ **Logs User Behavior** (Name, Email, IP, Device, etc.)  
✅ **Automated Execution** via **GitHub Actions**  

---

## 🚀 Installation Guide

### 🔹 **1. Clone the Repository**
```bash
git clone https://github.com/abhijeet-anand-quanmatic/selenium-automated-browser.git
cd selenium-automated-browser

🔹 2. Set Up Virtual Environment (Optional but Recommended)

python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

🔹 3. Install Dependencies

pip install -r requirements.txt

🏃 Usage

🔹 Run the Selenium Bot Locally

python script.py

This will:
	•	Open Quanmatic.com
	•	Scroll for 10-50 seconds
	•	Click random links
	•	Save session details

🔹 Stop the Script
	•	Press CTRL + C in the terminal

🛠 GitHub Actions Automation

This bot runs every hour via GitHub Actions:
	•	Runs automatically every hour (cron: '0 * * * *')
	•	Can be triggered manually
	•	Executes in headless mode on GitHub servers

📂 Workflow Configuration

The GitHub Actions workflow is located in:

.github/workflows/selenium.yml

To trigger the bot manually:
	1.	Go to GitHub Actions
	2.	Select Selenium Bot Automation
	3.	Click Run Workflow

📜 Project Structure

📦 selenium-automated-browser
│-- 📜 README.md           # Documentation
│-- 📜 requirements.txt    # Dependencies
│-- 📜 script.py           # Main Selenium bot script
│-- 📂 .github/workflows   # GitHub Actions configuration
│   ├── selenium.yml


📜 License

This project is licensed under the MIT License.


