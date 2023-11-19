## Sainofo Fanene
## Date: 11.12.23
## Personal Project: Email Slicers

print("Hello! Welcome!") ##intro

## asking for your email
email = input("Enter you email: ").strip()

## getting username and domain by string slicing
username = email[:email.index('@')]
domain = email[email.index('@')+ 1:]

## Displays the username and domain
print(f"Username: {username}")
print(f"Domain: {domain}")
