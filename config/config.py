from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv('gemini_api_key')
sender_gmail = os.getenv("sender_gmail")
google_app_pass = os.getenv("google_app_pass")
resume_path = "config/My Resume.pdf"



prompt = """
Generate an simple email body for a job application inquiry(asking if any internship/entry level job is available), focusing on backend or Python internship opportunities. The email should include body based on the following resume details:

- Applicant: Prashant Paneru
- Education: Currently pursuing Bachelor's in Information Technology
- Key Skills: Python, Django, Django Rest Framework, Web Scraping (Scrapy, Selenium, BeautifulSoup), Numpy, Pandas, Matplotlib, DSA
- Notable Projects: Call Record API, Social Media Web App, IMDB Scraper, Terminal Text Editor
- Experience: Currently freelancing at Parsedom (Data Scraping company), previous internship in software development
- github: https://www.github.com/pr45h4nt
- website: https://www.prashant69.com.np
- linkedin: https://www.linkedin.com/in/prashantpaneru/

Guidelines:
- Mention that this is for asking if any internship/entry level job is available.
- Don't include subject of the email. Include the body of the email only in your response
- DON'T USE ANY PLACEHOLDERS. Email body should be ready to send.
- Write in a style appropriate for a Bachelor's student
- Use direct and specific language
- Keep the tone professional yet enthusiastic


The email should:

- Inquire about available backend or Python internship positions
- say directly that if there is any opportunities I am a good candidate

Please provide the email content (body only) without any additional commentary.

"""