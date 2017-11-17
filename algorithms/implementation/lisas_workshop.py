total_chapters, total_problems_per_page = map(
    int,
    input().split()
)

chapter_pages = list(
    map(
        int,
        input().split()
    )
)


def get_workbook_iterator(
        chapters,
        problems_per_page,
        chapter_problems
):
    current_page = 1
    
    for current_chapter in range(1, chapters + 1):
        total_chapter_problems = chapter_problems[current_chapter - 1]
        page_problem = 0
        
        for problem_number in range(1, total_chapter_problems + 1):
            page_problem += 1
            
            if page_problem == problems_per_page + 1:
                page_problem = 1
                current_page += 1
            
            yield current_page, problem_number
        
        current_page += 1


workbook_iterator = get_workbook_iterator(
    total_chapters,
    total_problems_per_page,
    chapter_pages
)

special_problems_count = 0

for page, problem_number in workbook_iterator:
    if page == problem_number:
        special_problems_count += 1

print(special_problems_count)
