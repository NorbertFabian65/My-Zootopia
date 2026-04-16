import json


def load_data(file_path):
    """Lädt die JSON-Daten aus der Datei."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Erstellt einen HTML-String für ein einzelnes Tier."""
    output = ''
    output += '<li class="cards__item">\n'

    # Name des Tieres
    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    output += '  <p class="card__text">\n'
    output += '    <ul class="animal-details">\n'

    # Fundort (Location) - Wir nehmen das erste Element der Liste
    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'      <li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'

    # Merkmale aus "characteristics" (Beispiel: Diet und Type)
    characteristics = animal_obj.get("characteristics", {})
    if "diet" in characteristics:
        output += f'      <li><strong>Diet:</strong> {characteristics["diet"]}</li>\n'
    if "type" in characteristics:
        output += f'      <li><strong>Type:</strong> {characteristics["type"]}</li>\n'

    output += '    </ul>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    # 1. Daten laden
    animals_data = load_data('animals_data.json')

    # 2. HTML-String für alle Tiere generieren
    animals_html = ""
    for animal in animals_data:
        animals_html += serialize_animal(animal)

    # 3. Vorlage lesen
    with open("animals_template.html", "r") as f:
        template_content = f.read()

    # 4. Platzhalter in der Vorlage ersetzen
    # WICHTIG: Prüfe in deiner animals_template.html, wie der Platzhalter genau heißt!
    # Meistens ist es __REPLACE_ANIMALS_INFO__
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # 5. Die neue HTML-Datei speichern
    with open("animals.html", "w") as f:
        f.write(new_html_content)
    print("Webseite wurde erfolgreich unter 'animals.html' generiert!")


if __name__ == "__main__":
    main()