from django.shortcuts import render  
from django.http import HttpResponse  
from reportlab.pdfgen import canvas
def index(request):
    return render(request,"index.html")
def setsession(request):
    request.session['sname']='anu'
    request.session['semail']='anu@gmail.com'
    return HttpResponse("session set successfully")
def getsession(request):
    studentname=request.session['sname']
    studentmail=request.session['semail']
    return HttpResponse(studentname+" "+studentmail)
def getpdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment;filename="file.pdf"'
    p=canvas.Canvas(response)
    p.setFont('Times-Roman',55)
    p.drawString(200,200,"Hello world")
    p.showPage()
    p.save()
    return response
