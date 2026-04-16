import json


def load_data(file_path):
    """ Lädt eine JSON-Datei """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    # 1. Daten laden
    animals_data = load_data('animals_data.json')

    # 2. String mit den Tierdaten erzeugen (wie in Schritt 1, aber als String)
    output = ''
    for animal in animals_data:
        if "name" in animal:
            output += f"Name: {animal['name']}\n"

        characteristics = animal.get("characteristics", {})
        if "diet" in characteristics:
            output += f"Diet: {characteristics['diet']}\n"

        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"Location: {animal['locations'][0]}\n"

        if "type" in characteristics:
            output += f"Type: {characteristics['type']}\n"

        output += "\n"  # Leerzeile für den Abstand im Text

    # 3. Inhalt der Vorlage (Template) lesen
    with open("animals_template.html", "r") as f:
        template_content = f.read()

    # 4. Platzhalter __REPLACE_ANIMALS_INFO__ durch Tierdaten ersetzen
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    # 5. Den neuen HTML-Inhalt in die Datei 'animals.html' schreiben
    with open("animals.html", "w") as f:
        f.write(new_html_content)

    print("Die Datei animals.html wurde erfolgreich erstellt!")


if __name__ == "__main__":
    main()