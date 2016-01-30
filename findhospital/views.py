# Create your views here.
from file_read import read
from django.http import HttpResponse
from django.template import Template, Context
from geopy import geocoders
import geocoder
#from models import HospitalGeneralInformation, HospitalPerformance
import MySQLdb as msdb
import sys
from pyzipcode import ZipCodeDatabase


class hospitals(object):
    def __init__(self,provider_id,hospital_name,score):
        self.provider_id=provider_id
        self.hospital_name=hospital_name
        self.score=score


def connect():
    try:
        conn=msdb.connect('','root','password','hospital')
        return conn
    except Exception as e:
        return HttpResponse("Error DB")


def home(request):
    #g = geocoders.GoogleV3()
    #place, (lat, lng) = g.geocode('Charlotte')
    #g = geocoder.google([32.23, -80.8433], method='reverse')

    code = read('/home/sairam/Desktop/healthapp/findhospital/templates/index.html')
    t= Template(code)
    c = Context()
    return HttpResponse(t.render(c))
    
def hospital(request):
    g = geocoders.GoogleV3()
    place, (lat, lng) = g.geocode('Charlotte')
    g = geocoder.google([request.GET['latitude'], request.GET['longitude']], method='reverse')
    zcdb = ZipCodeDatabase()


    conn=connect()
    cur=conn.cursor()
    zip_list = zcdb.get_zipcodes_around_radius(g.postal, 35)    
    results=[]
    
    for z in zip_list:
#    	print z.zip

    	cur.execute("select f1.provider_id,f1.hospital_name,f2.score from (select * from findhospital_hospitalgeneralinformation where hospital_type='"+ request.GET['type']+" ' and zip_code = '"+ z.zip +"') as f1, findhospital_hospitalperformance f2  where f1.provider_id=f2.provider_id");

	for row in cur.fetchall():
		results.append(hospitals(row[0],row[1],row[2]))
		
    conn.close()


    for i in range( 1, len( results ) ):
    	obj = results[i]
    	tmp = results[i].score
    	print results[i].score
	k = i
	while k > 0 and tmp > results[k - 1].score:
        	results[k] = results[k - 1]
        	k -= 1
	results[k]=obj
    #for z in zip_list:
    #	print z.zip
       																																																							
    

    code = read('/home/sairam/Desktop/healthapp/findhospital/templates/results.html')
    t= Template(code)
    c = Context({'results':results})
    return HttpResponse(t.render(c))
    
    
    
    



