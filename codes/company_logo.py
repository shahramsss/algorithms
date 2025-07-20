def check_company_name(name):
    frequency = {}

    for letter in name:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    frequency_sorted = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    for k, v in frequency_sorted[:3]:
        print(k, v)
