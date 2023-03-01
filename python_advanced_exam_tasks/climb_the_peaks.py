from collections import deque

food_portions = deque([int(x) for x in input().split(", ")])
stamina = deque([int(x) for x in input().split(", ")])

conquered_peaks = []

mountain_peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

while food_portions and stamina:
    if len(conquered_peaks) == 5:
        break

    daily_portion = food_portions.pop()
    daily_stamina = stamina.popleft()
    current_sum = daily_portion + daily_stamina
    current_peak = mountain_peaks.popleft()

    if current_sum >= current_peak[1]:
        conquered_peaks.append(current_peak[0])
    else:
        mountain_peaks.appendleft(current_peak)

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep="\n")
