from validator_collection import validators, checkers, errors
# propmpt the use for an email address
user_input = input("What's your email address? ")
# check if input is a valid email
if is_email_address := checkers.is_email(user_input):
    print('Valid')
else:
    print('Invalid')


