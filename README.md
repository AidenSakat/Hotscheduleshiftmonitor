# Shift Checker Bot

This Python script automates the process of logging into a website, checking for available shifts, and notifying the user if shifts are available. The bot is designed to track shifts on a schedule, automatically pick them up if enabled, and send notifications to the user about available shifts.

## Requirements

- Python 3.x
- Selenium
- Plyer (for notifications)
- WebDriver for Chrome (make sure you have ChromeDriver installed)

## Setup

1. **Install the required libraries**:
    ```bash
    pip install selenium
    ```

2. **Download and install ChromeDriver**:
    - Ensure that ChromeDriver is installed and matches the version of your Chrome browser. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).
    - Add ChromeDriver to your system's PATH or specify its location in the script.

3. **Configure your settings**:
    - In the `config.py` file, set your `URL`, `USERNAME`, `PASSWORD`, and other configuration settings like `auto_pickup`, `off_days`, `NOTIFICATION_TIMEOUT`, and `REFRESH_PAGE`.

## File Structure

- `imports.py`: Contains all the necessary imports and modules.
- `config.py`: Configuration file to store sensitive data and settings (e.g., login credentials, preferences).
- `main.py`: Main script that performs login, checks shifts, sends notifications, and auto-picks up shifts.

## Script Overview

The script performs the following actions:

1. **Login**: Logs into the website using the provided username and password.
2. **Check for Available Shifts**: Continuously checks for available shifts, starting from the current day and checking future days.
3. **Notify User**: Sends a notification if a shift is available for a day that is not in the `off_days` list.
4. **Auto Pick-Up (Optional)**: If enabled in the config, the script will automatically pick up available shifts.
5. **Page Refresh**: After each check, the page is refreshed to ensure the latest shift data is retrieved.

## How to Use

1. Set up your `config.py` with the necessary credentials and settings.
2. Run the script:
    ```bash
    python shift_checker.py
    ```

3. The script will continuously monitor available shifts and notify you based on the configured settings.

## Example Configuration (config.py)

```python
URL = "https://example.com"
USERNAME = "your_username"
PASSWORD = "your_password"

# List of days you do not want to pick up shifts
off_days = ["Saturday", "Sunday"]

# Notification timeout in seconds
NOTIFICATION_TIMEOUT = 5

# Auto pickup shift if available (True or False)
auto_pickup = True

# Frequency of page refresh in seconds
REFRESH_PAGE = 60
