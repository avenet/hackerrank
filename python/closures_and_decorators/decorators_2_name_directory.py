def person_lister(f):
    def age_comparer(person):
        return int(person[2])

    def inner(person_list):
        people_sorted_by_age = sorted(
            person_list,
            key=age_comparer
        )

        return list(
            map(
                f,
                people_sorted_by_age
            )
        )

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
