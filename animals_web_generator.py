import json

def load_data(file_path):
    """ Lädt die JSON-Daten aus der Datei. """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

def serialize_animal(animal_obj):
    """ Erstellt einen HTML-String für ein einzelnes Tier. """
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += '    <ul class="animal-details">\n'
    
    # Beispiel für Details aus den "characteristics"
    characteristics = animal_obj.get("characteristics", {})
    if "diet" in characteristics:
        output += f'      <li><strong>Diet:</strong> {characteristics["diet"]}</li>\n'
    if "type" in characteristics:
        output += f'      <li><strong>Type:</strong> {characteristics["type"]}</li>\n'
    
    # Beispiel für den ersten Standort
    if animal_obj.get("locations"):
        output += f'      <li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'
        
    output += '    </ul>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output

animals_html = ""
for animal in animals_data:
    animals_html += serialize_animal(animal)

# Vorlage lesen
with open("animals_template.html", "r") as f:
    template_content = f.read()

# Platzhalter ersetzen
new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

with open("animals.html", "w") as f:
    f.write(new_html_content)

