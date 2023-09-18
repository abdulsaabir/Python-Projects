import requests 
import hashlib
import sys


def request_api_dat(query_char):
    url = 'https://api.pwnedpasswords.com/range/'  +  str(query_char)
    response = requests.get(url)
    if response.status_code != 200:
        print('error fetching data')
        return

    return response

def get_password_leaks_count(hashes,our_hash):
    splitted_hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in splitted_hashes:
        if h == our_hash:
            return count
    return 0

    

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5char, tail = sha1password[:5], sha1password[5:]
    response = request_api_dat(first_5char)

    return get_password_leaks_count(response,tail)


def main(args):
    for password in args:
        result = pwned_api_check(password)
        if result:
            print('your password {} has been leaked {} times'.format(password, result))
        else:
            print('this password {} hasn\'t been leaked'.format(password))

        


if __name__ == "__main__":
    main(sys.argv[1:])

