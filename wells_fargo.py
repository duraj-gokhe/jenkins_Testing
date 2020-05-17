import requests
from bs4 import BeautifulSoup
import json

def read():

	url = "https://employment.wellsfargo.com/psc/PSEA/APPLICANT_NW/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL?Page=HRS_APP_SCHJOB_FL&Action=U&"

	payload = {}
	headers = {
	  'Connection': 'keep-alive',
	  'Upgrade-Insecure-Requests': '2',
	  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
	  'Sec-Fetch-User': '?1',
	  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	  'Cookie': 'PS_DEVICEFEATURES=width:1600 height:900 pixelratio:1 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0; BIGipServeremployment_hrps_prod_443=330857226.27675.0000; employment_443_infra_2=!4/rfX8iBgEXQpURYv/e++mr64xsNwW2AEWMD//jFc14GDYsSZVrtbzoieKKjd/xPdUQIUTTyfGY5b7Y=; TS0106c80a=011a85ef9bbcc70af41e3c141f87d3d1b0bac52a72825db5f07322a9df72f55054d6bbcb29a609078a915b054b0aac92556e2d47c276167ab078d6a0390c2e91e2769f5ab8141a4af6d5a4d6c2c1307d5984f179c8; employment_443_infra_1=!9nd6vYH98FepNh1Yv/e++mr64xsNwZwFOvayRTKCijQuEKmuBFZQ3Hfb/9CIGGq+e+JPhtuhFh6mKi4=; PS8SMNSV702-7010-PORTAL-PSJSESSIONID=BsrvTulXpiRKXDp_jMg0o3YnkULIF0sy!-1669211114; ExpirePage=https://employment.wellsfargo.com/psc/PSEA/; PS_LOGINLIST=https://employment.wellsfargo.com/PSEA; PS_TOKEN=qQAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4AdQg4AC4AMQAwABSVMQZq5TitlwT4shCzjIsbfxEVRWkAAAAFAFNkYXRhXXicHYpLDkBAEAXLEEsr1yA+I5mtiF8iIljYOYXbOZw3ulP1upP3AFFogkD5Gv5JL1o27cJMp3vlJO4VI8nGwaD/ZmLHVhR4MlHKFU4uachlJ1tq2Sk9vs0H9SkMrw==; PS_TokenSite=https://employment.wellsfargo.com/psc/PSEA/?PS8SMNSV702-7010-PORTAL-PSJSESSIONID; SignOnDefault=; PS_LASTSITE=https://employment.wellsfargo.com/psc/PSEA/; ps_theme=node:HRMS portal:APPLICANT_NW theme_id:DEFAULT_THEME_FLUID css:PT_BRAND_CLASSIC_TEMPLTE_FLUID css_f:PT_BRAND_FLUID_TEMPLATE_857 accessibility:N macroset:PT_DEFAULT_MACROSET_857_NW formfactor:3 piamode:2; psback=%22%22url%22%3A%22https%3A%2F%2Femployment.wellsfargo.com%2Fpsc%2FPSEA%2FAPPLICANT_NW%2FHRMS%2Fc%2FHRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL%3Fpage%3DHRS_APP_SCHJOB_FL%22%20%22label%22%3A%22Search%20Jobs%22%20%22origin%22%3A%22PIA%22%20%22layout%22%3A%221%22%20%22refurl%22%3A%22https%3A%2F%2Femployment.wellsfargo.com%2Fpsc%2FPSEA%2FAPPLICANT_NW%2FHRMS%22%22; PS_TOKENEXPIRE=29_Jan_2020_03:20:27_GMT; TS013c8732=011a85ef9be2736617d6e8166026db11b176a66835825db5f07322a9df72f55054d6bbcb29292cbd776dbc1554bb2963dd8c3256acfc24129839130e9145f1d622b960e0ff25076b50ac3b2c19329523fdf1e7bbfec51085afb81357666dfb9feae13431c622b741799afa79a8549e6f57a97b89a76ebf99d9f538f060087be7e12eec8d8ac36fd3bb6dee0b3dbfcdd17809432758658279cdfee9ed5b14c4d980fac2003057b9b8597fdfad57fd5995e089c500f83c0471cd6d74fb953d57e2269f427d81'
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	soup = BeautifulSoup(response.text, 'lxml')
	# print(soup)
	a = soup.find('div', {'title':'Search Results List'}); b = a.find('ul', {'class':'ps_grid-body'})
	lis = b.find_all('li', {'class':'ps_grid-row psc_rowact'})
	print(len(lis))
	# print(lis[1])
	for i, data in enumerate(lis):
		title = data.find('span', {'id':"SCH_JOB_TITLE$" + str(i)}).text
		postedDate = data.find('span', {'id':'SCH_OPENED$' + str(i)}).text
		location = data.find('span', {'id':'LOCATION$'+str(i)}).text
		expiryDate = data.find('span', {'id':'HRS_JO_PST_CLS_DT$'+str(i)}).text
		category = data.find('span', {'id':'JOB_FAMILY_LABEL$'+str(i)}).text
		print(title)
		print(location)
		print(category)
		print(postedDate)
		print(expiryDate)
		print('---------------\n')

read()
