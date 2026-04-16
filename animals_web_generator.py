import json


def load_data(file_path):
    """ Lädt eine JSON-Datei """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    # Daten laden
    animals_data = load_data('animals_data.json')

    # Durch die Tiere iterieren
    for animal in animals_data:
        # 1. Name ausgeben (immer vorhanden laut JSON)
        if "name" in animal:
            print(f"Name: {animal['name']}")

        # 2. Ernährung (Diet) - liegt innerhalb von 'characteristics'
        characteristics = animal.get("characteristics", {})
        if "diet" in characteristics:
            print(f"Diet: {characteristics['diet']}")

        # 3. Den ersten Ort aus der Liste 'locations'
        if "locations" in animal and len(animal["locations"]) > 0:
            print(f"Location: {animal['locations'][0]}")

        # 4. Typ (Type) - ebenfalls in 'characteristics'
        if "type" in characteristics:
            print(f"Type: {characteristics['type']}")

        # Leerzeile für die Lesbarkeit zwischen den Tieren
        print("")


if __name__ == "__main__":
    main()