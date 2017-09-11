from math import (
    atan2,
    degrees
)

ab_side = int(input())
bc_side = int(input())

mbc_angle = degrees(
    atan2(ab_side, bc_side)
)

print(
    '{}°'.format(
        int(round(mbc_angle))
    )
)
