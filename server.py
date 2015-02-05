import urllib2
from bs4 import BeautifulSoup
import os
import json



class Spy():
	def callback(self):
		print "Scraping Banco Central"
		of = open('domain.text', 'w')
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
			key = key.replace("Observado","Observado ")


			value =  value[0].find("span").text.encode("utf-8")
			listado.append({"name": key, "value": value})
			
		return listado






from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class IndicadorREST(restful.Resource):
    def get(self):
         
    	s = Spy()
        return s.callback()

api.add_resource(IndicadorREST, '/')

if __name__ == '__main__':
    app.run(debug=False)
