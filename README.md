Installation
Step 1: Clone the Repository
Start by cloning the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/shift-pickup-automation.git
Step 2: Install Dependencies
Navigate to the project directory and install the required Python packages using pip:

bash
Copy code
cd shift-pickup-automation
pip install -r requirements.txt
Step 3: Download ChromeDriver
Download the version of ChromeDriver that matches your version of Google Chrome from the following link:
ChromeDriver Downloads

Once downloaded, place the chromedriver executable in the project directory or add its path to the system environment variables.

Configuration
Step 1: Set Up Configuration File
Before running the script, you'll need to set up the configuration file (config.py). In this file, define the following:

URL: The URL of the website you need to log into.
USERNAME: Your username for the website.
PASSWORD: Your password for the website.
OFF_DAYS: Days when you do not want to check for shifts (e.g., ["Tue", "Wed"]).
AUTO_PICKUP: Set to True if you want the script to automatically pick up shifts when available, otherwise set it to False.
NOTIFICATION_TIMEOUT: Duration for how long the notification will appear on the screen.
REFRESH_PAGE: Time in seconds between each page refresh to check for updated shifts.
Example configuration:

python
Copy code
URL = "https://example.com"
USERNAME = "your_username"
PASSWORD = "your_password"
OFF_DAYS = ["Tue", "Wed"]
AUTO_PICKUP = True
NOTIFICATION_TIMEOUT = 5
REFRESH_PAGE = 60
Step 2: Adjust Chrome Options
The script is configured to run in a detached mode where the browser remains open after the script completes. If you want to close the browser automatically after execution, you can remove or adjust the chrome_options.add_experimental_option("detach", True) line in the script.

Running the Script
To run the script, simply execute the Python file:

bash
Copy code
python shift_pickup.py
The script will log in to the website, monitor available shifts, and send notifications when shifts are found or picked up. It will continue running in a loop, checking for new shifts and refreshing the page at the interval specified in the config.py file.
