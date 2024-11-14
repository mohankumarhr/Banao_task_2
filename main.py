from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv


twitter_links = ['https://twitter.com/GTNUK1', 'https://twitter.com/whatsapp', 'https://twitter.com/aacb_CBPTrade', 'https://twitter.com/aacbdotcom', 'https://twitter.com/@AAWindowPRODUCT', 'https://www.twitter.com/aandb_kia', 'https://twitter.com/ABHomeInc', 'https://twitter.com/Abrepro', 'http://www.twitter.com', 'https://twitter.com/ACChristofiLtd', 'https://twitter.com/aeclothing1', 'http://www.twitter.com/', 'https://twitter.com/AETechnologies1', 'http://www.twitter.com/wix', 'https://twitter.com/AGInsuranceLLC']


# with open('D:\\python\\Banao Selenium #2\\twitter_links.csv', mode='r') as file:
#     csv_reader = csv.reader(file)
    
    
#     for row in csv_reader:
       
#         twitter_links.append(row[0])




# Initialize the Chrome WebDriver
browser = webdriver.Chrome()

# Open Twitter login page
browser.get('https://twitter.com/GTNUK1')

# Wait for the page to load
sleep(5)

# Maximize the browser window
browser.maximize_window()

# Locate the username input field and enter the username
username = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
username.send_keys("your usern")

# Locate and click the "Next" button
next_button = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
next_button.click()

# Wait for the password field to appear
sleep(2)

# Locate the password input field and enter the password
password = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys("your password")

# Locate and click the "Login" button
login_button = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
login_button.click()

# Wait for the login process to complete
sleep(10)

# Initialize a list to store profile data
profileDetails = []

# Loop through each Twitter profile link
for link in twitter_links:
    # Open the Twitter profile page
    browser.get(link)
    sleep(5)
    
    # Create a dictionary to store data for the current profile
    new_data = {}

    # Attempt to retrieve the bio, if available
    try:
        new_data['bio'] = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/div/span').text
    except Exception as e:
        new_data['bio'] = ""  # Set to empty if not found

    # Attempt to retrieve the following count, if available
    try:
        new_data['following_count'] = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span').text
    except Exception as e:
        new_data['following_count'] = ""  # Set to empty if not found

    # Attempt to retrieve the followers count, if available
    try:
        new_data['followers_count'] = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span').text
    except Exception as e:
        new_data['followers_count'] = ""  # Set to empty if not found

    # Attempt to retrieve the location, if available
    try:
        new_data['location'] = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[1]/span/span').text
    except Exception as e:
        new_data['location'] = ""  # Set to empty if not found

    # Attempt to retrieve the website URL, if available
    try:
        new_data['website'] = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/a').get_attribute('href')
    except Exception as e:
        new_data['website'] = ""  # Set to empty if not found

    # Add the collected profile data to the profileDetails list
    profileDetails.append(new_data)

# Display the collected profile data
# print(profileDetails)

# Define the CSV file name
csv_file = 'ProfileDetails.csv'

# Define the headers for the CSV file
fieldnames = ['bio', 'following_count', 'followers_count', 'location', 'website']

# Open the CSV file for writing and save the profile data
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write the profile data rows
    writer.writerows(profileDetails)

# Confirm CSV file creation
print(f"CSV file '{csv_file}' created successfully!")

# Close the browser
browser.quit()

