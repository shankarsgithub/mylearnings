import xml.etree.ElementTree as etree
tree = etree.parse('C:\\Python36\\template.xml')
root = tree.getroot()
for child in root:
	print(child.tag)
	print(child.attrib)
	if child.tag=='mq_manager_configuration':
		child.attrib={'ccdt':'true'}
		print(child.attrib)
		
outxml = etree.tostring(root, method='xml')
print(etree.XML)
xml_file = open("D:\\Public\\Output.xml", "w")
xml_file.write("%s" % outxml)
xml_file.close()
