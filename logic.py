from collections import Counter

def predict_from_input(last_10_numbers):
    freq = Counter(last_10_numbers)
    top_freq = freq.most_common(3)

    mod = (last_10_numbers[-1] + last_10_numbers[-2]) % 10

    score = {}
    for n in range(10):
        score[n] = 0
        if n == mod:
            score[n] += 2
        if n in [x[0] for x in top_freq]:
            score[n] += 3
        if last_10_numbers.count(n) <= 1:
            score[n] += 1

    top2 = sorted(score.items(), key=lambda x: x[1], reverse=True)[:2]
    logic = "Frequency 📊 + Modulo 🔁 + Pattern 📈"
    return top2[0][0], top2[1][0], logic
