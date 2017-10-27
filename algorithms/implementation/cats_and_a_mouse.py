q = int(input().strip())


def get_mouse_trapper(cat_a_x, cat_b_x, mouse_x):
    distance_from_cat_a = abs(mouse_x - cat_a_x)
    distance_from_cat_b = abs(mouse_x - cat_b_x)
    
    if distance_from_cat_a < distance_from_cat_b:
        return 'Cat A'
    elif distance_from_cat_b < distance_from_cat_a:
        return 'Cat B'
    
    return 'Mouse C'


for a0 in range(q):
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]
    print(get_mouse_trapper(x, y, z))
