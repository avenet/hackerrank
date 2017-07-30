import math

ab = int(raw_input())
bc = int(raw_input())

ac = math.sqrt(ab ** 2 + bc ** 2)
mc = ac / 2
sin_mcb = ab / ac
bm = math.sqrt(2*(ab**2 + bc**2) - ac**2) / 2
sin_x = (mc * sin_mcb) / bm
x_rad = math.asin(sin_x)
x_deg = math.degrees(x_rad)

print '%s°' % int(round(x_deg))