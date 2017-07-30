#!/usr/bin/py
# Head ends here
def pairs(a,k):
    answer = 0
    unique_elements = set(a)
    for unique_element in unique_elements:
        if unique_element + k in unique_elements:
            answer += 1
    return answer


if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)