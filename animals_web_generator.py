import json


def load_data(file_path):
    """Lädt die JSON-Daten aus der angegebenen Datei."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    Verarbeitet ein einzelnes Tier-Objekt und gibt einen HTML-String zurück.
    Folgt der Struktur aus Schritt 4.
    """
    output = '<li class="cards__item">\n'

    # Tiername als Titel
    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    characteristics = animal_obj.get("characteristics", {})

    # Details hinzufügen, falls vorhanden
    if "diet" in characteristics:
        output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'      <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    if "type" in characteristics:
        output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    """Hauptprogramm: Steuert den gesamten Prozess."""
    # 1. Daten laden
    animals_data = load_data('animals_data.json')

    # 2. HTML-String für alle Tiere generieren
    animals_html = ""
    for animal in animals_data:
        animals_html += serialize_animal(animal)

    # 3. Vorlage lesen
    with open("animals_template.html", "r") as f:
        template_content = f.read()

    # 4. Platzhalter ersetzen
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # 5. Finale Datei speichern
    with open("animals.html", "w") as f:
        f.write(final_html)

    print("Webseite erfolgreich mit strukturierter Funktion generiert!")


if __name__ == "__main__":
    main()