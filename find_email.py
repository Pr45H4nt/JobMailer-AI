import re
import requests
from bs4 import BeautifulSoup

def get_emails_from_website(url):
    # Send a request to the website
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all the text from the website
    text = soup.get_text()

    # regular expression
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses in the text
    emails = re.findall(email_pattern, text)

    # Removing duplicates
    emails = list(set(emails))

    return emails

def search_all_pages(url):
    if url[-1] != '/':
        url += '/'
    pages = ['about','contact','about-us', 'contact-us', 'aboutus', 'contactus']
    emails = get_emails_from_website(url)
    if emails:
        return emails
    for page in pages:
        new_url = url + page
        emails = get_emails_from_website(new_url)
        if emails:
            return emails

if __name__ == "__main__":
    url = input("Enter the website URL: ")
    emails = get_emails_from_website(url)

    if emails:
        print("Email addresses found:")
        for email in emails:
            print(email)
    else:
        print("\033[91m No email addresses found.")
