import json


def load_data(file_path):
    """ Lädt eine JSON-Datei """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    # 1. Daten laden
    animals_data = load_data('animals_data.json')

    # 2. HTML-String mit Serialisierung erzeugen
    output = ''
    for animal in animals_data:
        # Jedes Tier beginnt mit einem Listenelement-Tag
        output += '<li class="cards__item">\n'

        if "name" in animal:
            output += f"  <div class=\"card__title\">{animal['name']}</div>\n"

        output += '  <p class="card__text">\n'

        # Details hinzufügen
        characteristics = animal.get("characteristics", {})
        if "diet" in characteristics:
            output += f"    <strong>Diet:</strong> {characteristics['diet']}<br/>\n"

        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"    <strong>Location:</strong> {animal['locations'][0]}<br/>\n"

        if "type" in characteristics:
            output += f"    <strong>Type:</strong> {characteristics['type']}<br/>\n"

        output += '  </p>\n'
        # Jedes Tier endet mit dem schließenden Tag
        output += '</li>\n'

    # 3. Vorlage lesen
    with open("animals_template.html", "r") as f:
        template_content = f.read()

    # 4. Ersetzen
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    # 5. Speichern
    with open("animals.html", "w") as f:
        f.write(new_html_content)

    print("Die Datei animals.html wurde mit HTML-Karten erstellt!")


if __name__ == "__main__":
    main()