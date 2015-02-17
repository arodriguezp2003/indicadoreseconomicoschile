import urllib2
from bs4 import BeautifulSoup
import os
import json



class Spy():
	def callback(self):
		print "Scraping Banco Central"
		url = 'http://si3.bcentral.cl/indicadoresvalores/secure/indicadoresvalores.aspx'

		page = urllib2.urlopen(url)
        
		soup = BeautifulSoup(page)
		
		u = soup.findAll("table")[0].findAll("tr")
		
		
		listado = []


		for d  in u:
			key =  d.findAll("td", { "class" : "Desc" })
			value =  d.findAll("td", { "class" : "Valo" })


			key =  key[0].find("span").text.encode("utf-8")
			
			key = key.replace("\xc3\x83\xc2\xb3","o")
			key = key.replace("Observado","")
			
			if "("  in key:
				key ="UTM"

			key = key.strip()

			value =  value[0].find("span").text.encode("utf-8")

			value = value.split(',')[0]

			value = value.replace(".",",")


			listado.append({"name": key, "value": value})
			
			
		return listado
	


from flask import Flask , render_template
from flask.ext import restful

app = Flask(__name__,static_url_path='')
api = restful.Api(app)

class restFull(restful.Resource):
    def get(self):
    	s = Spy()
        return s.callback(),201, {'Access-Control-Allow-Origin': '*'} 



@app.route('/')
def index():
	return render_template('index.html')


api.add_resource(restFull, '/api')

if __name__ == '__main__':
	app.debug = True
	print "Debug mode on"
	app.run(host='0.0.0.0', port=3000)

