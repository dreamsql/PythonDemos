import xml.etree.ElementTree as ET

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(b, 'c')
d = ET.SubElement(c, 'd')

xml = ET.tostring(a, encoding='utf-8',method='xml')

print xml
