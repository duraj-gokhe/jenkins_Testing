from sqlalchemy import create_engine
import urllib.parse
import requests


def db_connection():
	APP_CONNECTION_STRING = 'DRIVER={SQL Server};SERVER=tcp:cynaptxprodserver.database.windows.net;DATABASE=cynaptxproddb;UID=cynaptx@cynaptxprodserver;PWD=coke53@10'
	params = urllib.parse.quote_plus(APP_CONNECTION_STRING)
	connection_string = "mssql+pyodbc:///?odbc_connect=%s" % params
	engine = create_engine(connection_string)
	connection = engine.connect()
	query = "SELECT OnlineApplicationAddress FROM JobOrder JO WHERE JO.TenantId =1377 AND JO.OnlineApplicationAddress Is Not Null AND JO.ExternalOrganization != ' '"
	result = connection.execute(query)
	for row in result:
		for url in row:
			print(url)
			response = requests.get(url, verify = True)
			print(response)
db_connection()