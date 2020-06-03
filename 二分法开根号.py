a = 10.01

right = a
left = 0

while right - left > 0.001:
    next_middle = right - (right - left) / 2
    if next_middle * next_middle > a:
        right = next_middle
    else:
        left = left + (right - left) / 2

print(left)
