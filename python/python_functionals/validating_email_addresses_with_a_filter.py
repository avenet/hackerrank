def validate_username(username):
    char_validation_result = map(
        lambda c: c.isalpha() or c.isdigit() or c == '-' or c == '_',
        username
    )
    
    return all(char_validation_result)


def validate_website(website):
    char_validation_result = map(
        lambda c: c.isalpha() or c.isdigit(),
        website
    )
    
    return all(char_validation_result)


def validate_extension(extension):
    return len(extension) < 4


def fun(s):
    if '@' not in s:
        return False
    splitted_email = s.split('@')
    
    if len(splitted_email) != 2:
        return False
    
    username, host = splitted_email
    
    if not username:
        return False
    
    if not validate_username(username):
        return False
    
    splitted_host = host.split('.')
    
    if len(splitted_host) != 2:
        return False
    
    website, extension = splitted_host
    
    if not validate_website(website):
        return False
    
    if not validate_extension(extension):
        return False
    
    return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
