

product_type_map = {
	'1': 'Foreign Exchange',
	'2': 'Physical Product',
	'3': 'Future',
	'4': 'Precious Metals',
	'5': 'unknown'
}


def parse(source):
	items = source.split('|')
	i = 11
	count = len(items) 
	result = []
	while ( i < count - 2) :
		p_type = product_type_map[getValue(items[i + 1])]
		result.append('product = %s, type = %s' % (getValue(items[i]),p_type))
		i += 2
	return result

def getValue(pair):
	items = pair.split('=')
	return items[1]


if __name__ == '__main__':
	source = '8=FIX.4.4|9=1037|35=y|49=WINGFUNGSTRUAT|56=MKS_STR|52=20170726-08:55:56.514|34=2|320=164f61ff-df82-48b3-be3a-6664544e9fdc|560=0|893=N|146=50|55=AUKB999|1151=2|55=AUStd9999|1151=2|55=PTKB9995|1151=2|55=XAG/CHF|1151=4|55=XPT/GBP|1151=4|55=PLV6|1151=3|55=USD/SGD|1151=1|55=PLF6|1151=3|55=AU50G9999|1151=2|55=XAU/USD.FWD|1151=5|55=AU10BA965|1151=2|55=PAH6|1151=3|55=USD/CNH|1151=1|55=XAG/USD|1151=4|55=USD/MYR|1151=1|55=XAG/USD.FWD|1151=5|55=SIZ6|1151=3|55=AGKB999|1151=2|55=PLN6|1151=3|55=PTStd9995LDN|1151=2|55=XPT/CHF|1151=4|55=GCQ6|1151=3|55=AUHKB995|1151=2|55=PT50OZ999|1151=2|55=AUD/USD|1151=1|55=EUR/USD|1151=1|55=XAU/CNH|1151=4|55=AU50G999|1151=2|55=GCZ7|1151=3|55=GCJ7|1151=3|55=XPT/USD|1151=4|55=XAU/JPY|1151=4|55=EUR/CHF|1151=1|55=AU100G995|1151=2|55=SIK6|1151=3|55=AUSMGRFO|1151=2|55=XPT/EUR|1151=4|55=XAU/MYR|1151=4|55=PLF7|1151=3|55=PD100OZ999|1151=2|55=AUTT9999|1151=2|55=XPD/GBP|1151=4|55=PAU7|1151=3|55=USD/INR|1151=1|55=AU200G9999|1151=2|55=PTStd9995GR|1151=2|55=PDStd9995GR|1151=2|55=AU10BA9999|1151=2|55=AUKB9999|1151=2|55=USD/CHF|1151=1|10=237|'
	result = parse(source)
	print('products count = %d' % len(result))
	for item in result:
		print(item)



	