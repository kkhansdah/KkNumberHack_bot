from collections import Counter

def predict_numbers(last10):
    freq = Counter(last10)
    scores = {}

    for n in range(10):
        score = 0
        if freq[n] >= 2:
            score += 2
        if n == sum(last10[-5:]) % 10:
            score += 1
        for i in range(len(last10)):
            if last10[i] == n:
                gap = len(last10) - i
                if 2 <= gap <= 6:
                    score += 1.5
        if n == last10[-1]:
            score += 1.5
        if (n >= 5 and sum(1 for x in last10[-5:] if x < 5) >= 4) or (n < 5 and sum(1 for x in last10[-5:] if x >= 5) >= 4):
            score += 1

        scores[n] = round(score, 2)

    top3 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

    reply = "🎯 *अगला अनुमानित नंबर (Top 3):*\n\n"
    levels = ["🔵 Level 1", "🟢 Level 2", "🟣 Level 3"]
    for i, (num, sc) in enumerate(top3):
        reply += f"{levels[i]}: {num}  (Score: {sc})\n"
    reply += "\n📊 लॉजिक: Frequency 📈 + Modulo ➗ + Gap 🔁 + Trend 📐"
    reply += "\n📌 Smart Bet: Level 1 या 2\n🔥 Bonus: Try all 3 if sure profit!"

    return reply
