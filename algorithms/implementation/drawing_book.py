def get_sheet_turns(page):
    return page // 2


def min_page_turns(n, p):
    return min(
        abs(get_sheet_turns(n) - get_sheet_turns(p)),
        get_sheet_turns(p),
    )


n = int(input().strip())
p = int(input().strip())
print(min_page_turns(n, p))
