from tornado import httpclient






if __name__ == '__main__':

	client = httpclient.HTTPClient()
	response = client.fetch('http://www.baidu.com')
	print(response.body)
	