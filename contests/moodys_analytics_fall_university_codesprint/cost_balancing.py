#!/bin/python3

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    total_amount = 0
    person_balance = [0] * m

    for a0 in range(n):
        id_number, amount = input().strip().split(' ')
        id_number, amount = [int(id_number), int(amount)]
        total_amount += amount
        person_balance[id_number - 1] += amount

    anita_extra_money = total_amount % m
    money_per_person = total_amount // m
    person_balance[0] -= anita_extra_money
    
    for i in range(m):
        person_balance[i] -= money_per_person
        print('{} {}'.format(i + 1, person_balance[i]))
