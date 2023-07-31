import xml.etree.ElementTree as ET
import csv

path_file_kml = "D:\_TESTE\Mobile\DER_PR_KML\doc.kml"
file_name = "D:\_TESTE\Mobile\DER_PR_KML\dadosV4.csv"
count_id = -1
variable_is_id = False
variable_is_lot = False

tree = ET.parse(path_file_kml)
root = tree.getroot()

with open(file_name, mode='w', newline='') as file_csv:
    writer = csv.writer(file_csv, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(["ID", "NOME", "LONGITUDE", "LATITUDE", "RODOVIA", "TRECHO", "LOTE", "KM", "METRO"])

    for tag in root.iter():
        variable = tag.text
        if variable is not None and "ID-" in variable:
            variable_is_id = True
            content_name = f"{variable.split()[0]}_{variable.split()[1].replace('(', '').replace(')', '')}" 
            print("Conteúdo ID:", content_name)

        if variable is not None and "Lote " in variable and variable_is_id:
            variable_is_lot = True
            content_lot = variable.split()[1]
            content_highway = variable.split()[3]
            content_km = variable.split()[5]
            print("Conteúdo LOTE:", content_lot)
            print("Conteúdo RODOVIA:", content_highway)
            print("Conteúdo KM:", content_km)


        if variable is not None and ("." in variable or "," in variable) and variable_is_lot and variable_is_id:
            variable_is_id = False
            variable_is_lot = False
            count_id = count_id + 1
            content_latitude = variable.split(',')[1].replace('.', ',')
            content_longitude = variable.split(',')[0].replace('.', ',')

            content_name =  content_name + "_" + "L" + content_lot + "_" + content_highway

            content_meter = content_km.split('+')[1]
            content_km = content_km.split('+')[0]

            writer.writerow([count_id, content_name, content_longitude, content_latitude, content_highway, '', content_lot, content_km, content_meter])
            
            print("Conteúdo LATITUDE:", content_latitude)
            print("Conteúdo LONGITUDE:", content_longitude)
            print("\n\n")

        
