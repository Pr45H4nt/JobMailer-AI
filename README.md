# JobMailer-AI

JobMailer-AI is an automated job application system that helps streamline the process of sending personalized internship/job inquiries to multiple companies. It combines web scraping, AI-powered content generation, and automated email handling to efficiently reach out to potential employers.

## Features

- 🌐 **Automated Email Discovery**: Scrapes company websites to find relevant contact email addresses
- 🤖 **AI-Powered Email Generation**: Uses Google's Gemini AI to create personalized job inquiry emails
- 📧 **Automated Email Sending**: Handles email composition and sending with resume attachments
- 📝 **Manual Review System**: Allows review and editing of AI-generated emails before sending
- 📊 **Progress Tracking**: Maintains logs of contacted companies to prevent duplicate outreach

## Setup

1. Clone the repository
```bash
git clone https://github.com/pr45h4nt/jobmailer-ai.git
cd jobmailer-ai
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following variables:
```
gemini_api_key=your_gemini_api_key
sender_gmail=your_gmail_address
google_app_pass=your_google_app_password
```

4. Set up your resume:
- Place your resume PDF in the `config` folder
- Update the `resume_path` in `config/config.py` if needed

5. Update the prompt in `config/config.py`:
- Replace the example resume details with your own:
  ```python
  - Name
  - Education
  - Key Skills
  - Notable Projects
  - Experience
  - GitHub profile
  - Personal website (if any)
  - LinkedIn profile
  ```
- Customize the email tone and focus based on your preferences
- Modify the job position type (currently set for backend/Python internship)

6. Prepare company data:
- Create or upload a CSV file in the `data` folder named `companies.csv` with the given format
- Format: `Name,Website,Location,Keywords,Description`

## Usage

1. Update the email template in `config/config.py` if needed
2. Run the main script:
```bash
python main.py
```

3. For each company, the script will:
- Search for contact emails on the company website
- Generate a personalized email using AI
- Allow you to review and edit the email
- Send the email with your resume attached

## Project Structure

```
jobmailer-ai/
├── main.py           # Main orchestration script
├── find_email.py     # Email scraping functionality
├── send_email.py     # Email sending functionality
├── get_response.py   # Gemini AI integration
├── handle_logs.py    # Logging utilities
├── config/
│   ├── config.py     # Configuration and prompts
│   └── email.txt     # Generated email content
├── data/
│   └── companies.csv # Company information
└── logs/
    └── sent.txt     # Log of contacted companies
```

## Requirements

- Python 3.8+
- Google Gemini API key
- Gmail account with App Password enabled
- Internet connection for web scraping and API calls

## Security Notes

- Never commit your `.env` file
- Use environment variables for sensitive information
- Follow Gmail's security best practices
- Review emails before sending to ensure appropriate content

## Important Notes

1. **Personalization**: The success of this tool heavily depends on properly updating the prompt in `config.py` with your personal information. The current template includes example details that must be replaced with your own resume information.

2. **Email Content**: Always review the AI-generated emails before sending. The content should match your professional tone and accurately represent your skills and experience.

3. **Rate Limiting**: Consider adding delays between emails to avoid triggering spam detection.

## Contributing

Feel free to open issues or submit pull requests for any improvements.


## Disclaimer

Please ensure compliance with all applicable laws and regulations when sending automated emails. Be respectful of rate limits and company communication preferences.