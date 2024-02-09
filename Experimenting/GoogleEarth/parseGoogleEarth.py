import xml.etree.ElementTree as ET


kml_file_path = 'Experimenting\\GoogleEarth\\test.kml'

# Namespace used in KML files
ns = {'kml': 'http://www.opengis.net/kml/2.2'}

# Function to parse KML and print names and coordinates
def parse_kml(file_path):
    # Parse the KML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Find all placemarks in the KML file
    for placemark in root.findall('.//kml:Placemark', ns):
        name = placemark.find('kml:name', ns)
        if name is not None:
            name = name.text
        else:
            name = "No Name"

        # Extracting the coordinates
        coordinates = placemark.find('.//kml:coordinates', ns)
        if coordinates is not None:
     
            coord_text = coordinates.text.strip()

            # Coordinates are provided as longitude,latitude,altitude
            longitude, latitude, altitude = coord_text.split(',')
            print(f"Name: {name}, Coordinates: Latitude {latitude}, Longitude {longitude}")
        else:
            print(f"Name: {name} has no coordinates.")


parse_kml(kml_file_path)
