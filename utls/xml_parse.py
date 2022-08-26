import xml.etree.ElementTree as ET

tree = ET.parse('config.xml')
root = tree.getroot()