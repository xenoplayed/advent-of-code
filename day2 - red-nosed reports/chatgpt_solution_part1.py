def is_increasing(levels):
    """Prüft, ob die Zahlen in der Liste streng zunehmend sind."""
    return all(0 < levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))


def is_decreasing(levels):
    """Prüft, ob die Zahlen in der Liste streng abnehmend sind."""
    return all(0 < levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))


def is_safe_report(levels):
    """Prüft, ob eine Zeile sicher ist."""
    return is_increasing(levels) or is_decreasing(levels)


# Die gegebene Liste von Berichten
data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

# Prüfung der Daten
# unsafe_reports = []
safe_reports = []
for i, report in enumerate(data):
    if is_safe_report(report):
        safe_reports.append((i + 1, report))  # Speichere Zeilenindex und Inhalt
    # else:
    #     unsafe_reports.append((i+1, report))

# Ausgabe der sicheren Berichte
print(f"Safe reports: {len(safe_reports)}")
for idx, report in safe_reports:
    print(f"Report {idx}: {report}")

# print(f"Unsafe reports: {len(unsafe_reports)}")
# for idx, report in unsafe_reports:
#     print(f"Report {idx}: {report}")
