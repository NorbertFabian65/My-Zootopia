import json


def load_data(file_path):
    """ Lädt die JSON-Datei """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    # 1. Daten laden
    animals_data = load_data('animals_data.json')

    # 2. Finales HTML-Design generieren
    output = ''
    for animal in animals_data:
        # Start der Karte
        output += '<li class="cards__item">\n'

        # Titel der Karte
        if "name" in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'

        # Textbereich der Karte
        output += '  <p class="card__text">\n'

        characteristics = animal.get("characteristics", {})

        # Ernährung (Diet)
        if "diet" in characteristics:
            output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

        # Ort (Location)
        if "locations" in animal and animal["locations"]:
            output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

        # Typ (Type)
        if "type" in characteristics:
            output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

    # 3. Vorlage lesen
    with open("animals_template.html", "r") as f:
        template_content = f.read()

    # 4. Ersetzen
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    # 5. Speichern
    with open("animals.html", "w") as f:
        f.write(new_html_content)

    print("Glückwunsch! Das finale Design wurde in 'animals.html' gespeichert.")


if __name__ == "__main__":
    main()