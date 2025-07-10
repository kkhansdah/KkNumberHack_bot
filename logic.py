from collections import Counter

def mirror(n):
    mirror_map = {0:9, 1:8, 2:7, 3:6, 4:5, 5:4, 6:3, 7:2, 8:1, 9:0}
    return mirror_map.get(n, n)

def get_prediction(numbers):
    numbers = [int(n) for n in numbers if n.isdigit()]
    if len(numbers) < 5:
        return []

    freq = Counter(numbers)
    recent = numbers[-2:]  # Repeat block
    mirror_scores = Counter()
    gap_scores = Counter()
    modulo_scores = Counter()
    trend_scores = Counter()

    for i in range(len(numbers) - 1):
        gap = abs(numbers[i] - numbers[i + 1])
        gap_scores[gap] += 1

    for n in numbers:
        m = mirror(n)
        mirror_scores[m] += 1

    for n in numbers:
        modulo_scores[n % 3] += 1

    for i in range(len(numbers)):
        trend_scores[numbers[i]] += i / len(numbers)  # Recent numbers get higher score

    combined_scores = Counter()
    for n in range(10):
        if n in recent:
            continue  # last 2 numbers skip

        combined_scores[n] += freq[n] * 1.5
        combined_scores[n] += mirror_scores[n] * 1.4
        combined_scores[n] += gap_scores[n] * 1.2
        combined_scores[n] += modulo_scores[n % 3] * 1.0
        combined_scores[n] += trend_scores[n] * 1.3  # trend booster

    top3 = combined_scores.most_common(3)
    return [(num, round(score, 2)) for num, score in top3]
