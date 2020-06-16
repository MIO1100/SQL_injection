from django.shortcuts import render
from django.shortcuts import render_to_response
import MySQLdb
import re
# Create your views here.
def index(request):
    return render(request,'cyber/main_home.html', locals())
def info(request):
    return render(request,'cyber/main_info.html', locals())
def art(request):
    db = MySQLdb.connect(user='root', db='task', passwd='123456', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM new_schema.guns WHERE idguns<7;')
    names = [row[0] for row in cursor.fetchall()]
    cursor.execute('SELECT pictures FROM new_schema.guns WHERE idguns<7;')
    pictures = [row[0] for row in cursor.fetchall()]
    db.close()
    data = {"names": names, 'pictures': pictures}
    return render(request, 'cyber/main_art.html', context=data)

def search(request):
    return render(request, 'cyber/main_search.html', locals())


def search_proc(request):
    try:
        db = MySQLdb.connect(user='root', db='task', passwd='123456', host='localhost')
        cursor = db.cursor()
        z=request.POST.get('naz')
        cursor.execute('SELECT idguns FROM new_schema.guns WHERE name="' + str(z)+'";')
        res=id=str(cursor.fetchall())
        id= re.sub("[',()]", '', id)
        cursor.execute('SELECT pictures FROM new_schema.guns WHERE idguns="'+ id+'";')
        pictures = cursor.fetchall()
        db.close()
        picture=str(pictures[0])
        fi = ''.join(picture.split("'", ))
        fix = ''.join(fi.split(",", 2))
        fixe = ''.join(fix.split("(", 1))
        fixed = ''.join(fixe.split(")", 2))
        data = {'pictures': fixed, 'res': res}
        return render(request, 'cyber/main_search.html', context=data)
    except:
        return render(request, 'cyber/main_search.html', {'res':res})