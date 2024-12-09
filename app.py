import requests

def main():
    nickname = input('Enter nickname for search : ')
    emails = set()
    try:
        url = f'https://api.github.com/users/{nickname}/events/public'
        page = requests.get(url)

        if page.status_code == 200:
            if not page.json(): return 'email not found'
        elif page.status_code == 404: return f'user {nickname} - not found'
    except Exception as e:
        print(f"An error occurred: {e}")

    for element in page.json():
        if element ['type'] == 'PushEvent':
            for commit in element['payload']['commits']:
                email = commit['author']['email']
                emails.add(email)
    
    return f'Emails found :\n{emails}'

if __name__ == "__main__":
    print(main())