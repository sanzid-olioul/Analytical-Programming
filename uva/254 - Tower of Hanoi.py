from docx2pdf import convert
from pymongo import MongoClient
client = MongoClient("mongodb+srv://sanzid:854742879@cluster0.2mgrg.mongodb.net/test?retryWrites=true&w=majority")

db = client['pust']
collection = db['csestudents']
for d in collection.find():
    inpfl = 'all/'+str(d['roll'])+'.docx'
    outfl = 'another/'+str(d['roll'])+'.pdf'
    convert(inpfl,outfl)