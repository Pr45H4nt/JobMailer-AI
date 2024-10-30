from get_response import get_response
from config.config import gemini_api_key , google_app_pass , sender_gmail , prompt
from send_email import send_email
import csv
from find_email import search_all_pages
from handle_logs import check_logs , add_to_log



def write_and_send_email(receiver ,subject, extraprompt = ""):
    global prompt
    prompt = prompt
    gemini_api = gemini_api_key
    sender = sender_gmail
    sender_pass = google_app_pass
    prompt += extraprompt

    resp = get_response(gemini_api, prompt)

    print(resp)

    with open('config/email.txt', 'w') as f:
        f.write(resp)
    
    x = input("You can now edit your email body in config/emfileail.txt. "
               "Press 'N' for not sending this email. Press 'Q' for quitting the program. Press any other key to continue. : ")

    if x.lower() == "q":
        print("Quitting the program")
        quit()
    elif x.lower() == 'n':
        print("This email will not be sent. Continuing the program for next email.")
        return 


    with open('config/email.txt', 'r') as f:
        e_body = f.read()

    send_email(sender=sender , sender_pass= sender_pass, receiver=receiver, e_subject=subject, e_body=e_body)



with open('data/companies.csv', mode='r') as file:
    companies = csv.reader(file)
    for company in companies:
        site = company[1]
        if check_logs(site):
            print(f"Email Already sent to: {site}")
            continue
        emails = search_all_pages(site)
        print(f"""
              Company Name- {company[0]}
              Company website - {site}
              --Emails--
              {emails or "No email found"}""")
        if emails:
            email = emails[int(input("choose email index (starts from 0): "))]
            extra_p = f"""company name: {company[0]} \n   About company: {company[4]}\n  company keywords : {company[3]}"""
            subject = f"Backend/Python Internship Opportunity Inquiry - {company[0]}"
            write_and_send_email(email ,subject, extra_p )
        add_to_log(site)


