testcases = int(raw_input())

element_set = None

for testcase in xrange(testcases):
    testcase_set = set(raw_input())
    if element_set is not None:
        element_set = element_set.intersection(testcase_set)
    else:
        element_set = testcase_set

print len(element_set)