# ChatGPT solution
import time


# Funktion zum Einlesen der Datei und Umwandeln in Listen
def read_coordinates_from_file(file_path):
    left_list = []
    right_list = []

    # Öffne die Datei und lese Zeile für Zeile
    with open(file_path, "r") as file:
        for line in file:
            left, right = map(int, line.split())  # Trenne Zahlen und konvertiere sie zu Integer
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list


# Funktion zur Berechnung der Gesamtdistanz
def calculate_total_distance(left_list, right_list):
    # Sortiere beide Listen
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    # Berechne die Summe der Abstände
    total_distance = sum(abs(a - b) for a, b in zip(sorted_left, sorted_right))
    return total_distance


# Hauptprogramm
if __name__ == "__main__":
    start_time = time.time()

    # Dateipfad angeben
    file_path = "coordinates.txt"  # Pfad zur Datei

    # 1. Lese die Koordinaten aus der Datei
    left_list, right_list = read_coordinates_from_file(file_path)

    # left_list = [3, 4, 2, 1, 3, 3]
    # right_list = [4, 3, 5, 3, 9, 3]

    # 2. Berechne die Gesamtdistanz
    total_distance = calculate_total_distance(left_list, right_list)

    # 3. Ausgabe der Ergebnisse
    print("Left list:", left_list)
    print("Right list:", right_list)
    print(f"Total distance: {total_distance}")
    end_time = time.time()
    print(f"Runtime: {end_time - start_time} seconds.")
