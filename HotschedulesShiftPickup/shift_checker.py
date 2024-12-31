from imports import *
from config import *

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
  
driver = webdriver.Chrome(options=chrome_options)

def login():
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loginusername"))).send_keys(USERNAME)
    driver.find_element(By.ID, "loginpassword").send_keys(PASSWORD)
    driver.find_element(By.ID, "loginBtn").click()

# Login to the site
login()

# Wait until the "Available Shifts" button is available and click it
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "Available Shifts1"))
).click()

# Main loop to keep checking for shifts
while True:
    containers = driver.find_elements(By.CLASS_NAME, "future")

    for container in containers:
        try:
            available_shifts = container.find_elements(By.CLASS_NAME, "shift-pickup-item")
            current_day = container.find_element(By.CLASS_NAME, "day-name").text
            shifts_count = len(available_shifts)

            # check if shift is available / > 0
            if shifts_count > 0:
                container.find_element(By.CLASS_NAME, "item-shifts-amount").click()
                
                # Wait for shift time to appear
                shift_time = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 
                        ".shifts-table-body .table-item.shift-time"))
                ).text
                
                # Send notification
                if current_day not in off_days:
                  notification.notify(
                      title=f"{shifts_count} shifts found on {current_day}",
                      message=f"Shift time: {shift_time}",
                      timeout=NOTIFICATION_TIMEOUT
                  )
                  # Will auto pickup shift if availabe and notify you. Can disable in config
                  if auto_pickup:
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".echo-component-EchoButton-2670g.echo-component-footer-2KDZu"))
                    ).click()
                    notification.notify(
                      title=f"PICKED UP {current_day}",
                      message=f"Shift time: {shift_time}",
                      timeout=NOTIFICATION_TIMEOUT
                  )

                # Close the "pick up shift tab" (ESC)
                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

            time.sleep(1)  # Short delay before processing the next container

        except Exception as e:
            print(f"Error processing day: {e}")
    
    # Wait before refreshing the page and checking again
    print("Waiting for the next check...")
    time.sleep(REFRESH_PAGE)  # Adjust this to the frequency of your checks (60 seconds here)

    # Refresh the page to get updated shifts
    driver.refresh()
    time.sleep(5)  # Wait for the page to reload before continuing
