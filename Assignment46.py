#Read xml file and print all lines, search specific tags

import xml.etree.ElementTree as ET

tree = ET.parse("D:\PythonWork\PythonWork\Data\country.xml")

root = tree.getroot()
#
# # print(ET.tostring(root, encoding='utf8').decode('utf8'))
#
# for neighbor in root.iter('neighbor'):
#     print(neighbor)
#     print(neighbor.attrib)
# #
# for country in root.findall('country'):
#     print(country.find('rank').text)
#     print(country.get('name'))



#
tree1 = ET.parse("D:\PythonWork\PythonWork\Data\cat.xml")

root1 = tree1.getroot()

# for title in root1.findall('cd'):
#     print(title)
#     print(title.find('title').text)
#     print(title.getchildren())
#     print("hello")

for child in root1:
    print(child.tag)
    for child1 in child:
        print(child1.get('TITLE'))
        # print(ET.dump(child1))
        print(child1.text)

# for child in root1.findall(".//"):
#     print(child.tag)
#     print(child.text)

# print(root1[0][1].text)