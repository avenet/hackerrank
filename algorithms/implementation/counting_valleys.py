step_count = int(input())
steps = input()

UP_STEP = 'U'
DOWN_STEP = 'D'

GROUND = 0
BELOW_GROUND = -1

NEUTRAL_VALLEY = 0
STARTING_VALLEY = 1

current_level = 0
found_valleys = 0
valley_search_status = 0


for current_step_index in range(step_count):
    current_step = steps[current_step_index]
    previous_level = current_level

    if current_step == UP_STEP:
        current_level += 1
    elif current_step == DOWN_STEP:
        current_level -= 1

    if current_level == BELOW_GROUND and current_step == DOWN_STEP:
        valley_search_status = STARTING_VALLEY
    elif valley_search_status == STARTING_VALLEY and current_step == UP_STEP and current_level == GROUND:
        found_valleys += 1
        valley_search_status = NEUTRAL_VALLEY

print(found_valleys)
