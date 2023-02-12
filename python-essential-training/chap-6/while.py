# secret = 'swordfish'
# pw = ''
# global count
# count = 0

# while pw != secret:
#     if count == 2:
#         print('\nFinal attempt!')
#     if count == 3:
#         print('\nSystem self destruct in 3...2...1!')
#         break
#     else:
#         pw = input("What's the secret word? ")
#         count += 1

# if pw == 'swordfish':
#     print('\nYou have entered the correct password.')

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt: break
    if count == 3: continue # Only gives four tries instead of five
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

print('Authorized' if auth else 'Calling the FBI ...')
