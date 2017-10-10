def wrapper(f):
    def prettify(phone_number):
        return '{} {} {}'.format(
            phone_number[0:3],
            phone_number[3:8],
            phone_number[8:13]
        )

    def standardize_mobile_phone(phone_number):
        if not phone_number.startswith('+91'):
            if phone_number.startswith('0'):
                phone_number = '+91' + phone_number[1:]
            elif phone_number.startswith('91'):
                if len(phone_number) == 10:
                    phone_number = '91' + phone_number

                phone_number = '+' + phone_number
            else:
                phone_number = '+91' + phone_number
        return prettify(phone_number)

    def fun(phone_numbers):
        return f(
            [
                standardize_mobile_phone(phone_number)
                for phone_number
                in phone_numbers
            ]
        )

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
