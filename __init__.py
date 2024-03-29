# -*- coding: utf-8 -*-
"""This module contains a template MindMeld application"""
from mindmeld import Application

app = Application(__name__)

__all__ = ['app']



@app.handle(default=True)
def default(request, responder):
    """This is a default handler."""
    responder.reply('Hello there!')

@app.handle(intent='get_sal')
def salary(request,responder):
    print(request)
    #print()
   # print(request.text)
    print()
    askedcompany = request.entities[0]['value'][0]['cname']
    print(askedcompany)
    cnames = app.question_answerer.get(index='companies') 
    print(cnames)
    sals = []
    years = []
    for i in cnames:
       if i['company_name'].lower() == askedcompany.lower():
            sals = i['sals']
            years =i['years']
            print('Found')
            break
    print(sals)
    print(years)
    sals = list(sals.split())
    years =list(years.split())
    for i in range(len(years)):
       r = "The \"" + askedcompany + "\" gave a salary of " + sals[i] + " in the year " + years[i]
       print(r)    

@app.handle(intent='unsupported')
def notvalid(request,responder):
    responder.reply("Could n't get you")

@app.handle(intent='greet')
def greeting(request,responder):
    responder.reply('Hi I am your placementInfo Assistant')

@app.handle(intent='get_year')
def getyear(request,responder):
    print(request)
    askedcompany = request.entities[0]['text']
    years = []
    cnames = app.question_answerer.get(index='companies')
     
    for i in cnames:
       if i['company_name'].lower() == askedcompany.lower():
            years =i['years']
            print('Found')
            break
    years = list(years.split())
    print(askedcompany,"came in the following years",end = " ")
    for i in years:
        print(i,end = " ")


@app.handle(intent='get_sal_year')
def getsalyear(request,responder):
    conyear = request.frame.get('year')
    print(request.frame.get('year'))
    print(type(responder))
    askedcompany = "Not"
    askedyear = "-1"    
    #print(request.history[0]['request']['entities'])
          
    print("hist type",type(askedyear))
    for i in request.entities:
        if i['type'] == 'companies':
            print("1stfor",i)
            askedcompany = i['value'][0]['cname']
            break
    for i in request.entities:
        print("2ndfor",i)
        if i['type'] == 'sys_time':
            askedyear = i['text']
            print(i['text'])

    if conyear == None or (conyear != askedyear and askedyear!="-1"):
        conyear = askedyear
        responder.frame['year'] = conyear


    print(askedcompany,askedyear)
   
    if askedcompany == "Not":
        responder.reply("please tell the company Name")
        responder.frame['year'] = conyear
        responder.listen()
    else:
       print("Inside")
       print(askedyear,conyear) 
       cnames = app.question_answerer.get(index='companies') 
       print(cnames)
       flag = 0
       info = None
       for i in cnames:
            print(i['company_name']," +++++ " ,i['years'])
            if i['company_name'].lower() == askedcompany.lower() and (conyear in i['years']) :
                info = i
                print(i)
                print('Found')
                flag = 1
                break
       years = list(info['years'].split())
       sals = list(info['sals'].split())
       req = 0 
       for i in range(len(years)):
           if years[i] == conyear:
                req = sals[i]
                break
       responder.reply(askedcompany +" gave a salary of " + req + " in the year " + conyear)        
        

@app.handle(intent='get_companies')
def getcompanies(request,responder):
    cnames = app.question_answerer.get(index='companies')
      
    arr = [ i['company_name']  for i in cnames]
    
    r = "The Companies which came are " + " ".join(arr)
    responder.reply(r)







def printdash():
    print("---------------------------")








