def add_to_log(website):
    with open('logs/sent.txt', 'a') as f:
        f.write(website + '\n')

def check_logs(website):
    with open('logs/sent.txt', 'r') as f:
        webs = f.readlines()

    for i in webs:
        if i.strip() == website:
            return True
    return False
