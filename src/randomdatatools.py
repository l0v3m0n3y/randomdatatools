import requests
class Client():
	def __init__(self):
		self.api="http://api.randomdatatools.ru"
		#gender=man ,woman,unset . type=classic,rare,all . count = 1-100
	def get_name(self,gender:str,type:str,count: str="1",unescaped: str="false"):
		return requests.get(f"{self.api}?gender={gender}&typeName={type}&count={count}&unescaped={unescaped}").json()