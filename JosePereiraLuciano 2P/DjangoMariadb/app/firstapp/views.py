from django.shortcuts import render, HttpResponse
from .models import Estados, Movie, ApiUsers
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import json
from firstapp.customClasses import *
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password

def paito(request):
    if request.method == 'GET':
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Metodo valido'
        return JsonResponse(response_data, status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Metodo invalido'
        return JsonResponse(response_data, status=403)

def results(request, id):
    event_list = Estados.objects.all()
    return HttpResponse("You're looking at %s." % event_list[id].name)
    return HttpResponse("You're looking at %s." % id)

def createsession(request):

    if request.method == 'POST':
        json_data = json.loads(request.body)
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = json_data["Has entrado!"]
        return JsonResponse(response_data, status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Metodo invalido'
        return JsonResponse(response_data, status=403)

def createpatient(request):
    if request.method == 'POST':
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Metodo valido'
        return JsonResponse(response_data, status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Metodo invalido'
        return JsonResponse(response_data, status=403)

def addclinicalcase(request):
    if request.method == 'POST':
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Metodo valido'
        return JsonResponse(response_data, status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Metodo invalido'
        return JsonResponse(response_data, status=403)

def addclinicalcasenote(request):
    
    if request.method == 'POST':
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Metodo valido'
        return JsonResponse(response_data, status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Metodo invalido'
        return JsonResponse(response_data, status=403)

def state(request, id):
    if request.method == 'GET':
        respnse_data == {}
        try:
            obj = Estados.objects.get(id = id)
            response_data['result'] = 'success'
            response_data['name'] = obj.name
            response_data['clave'] = obj.clave
            response_data['abrev'] = obj.abrev
            response_data['riskIndex'] = obj.risk
            return JsonResponse(response_data, status= 200)
        except Estados.DoesNotExist:
            response_data['result'] ='error'
            response_data['message'] ='No se encontro un id'
            return JsonResponse(response_data, status = 400)
    else:
        response_data = {}
        response_data['result'] = 'error'

def states(request):
 if request.method =='GET':
    response_data = {}
    response_data["estados"] = {}
    cont = 0
    for i in Estados.objects.all():
        response_data["estados"][cont] = {}
        response_data["estados"][cont]["name"] = i.name
        response_data["estados"][cont]['clave'] = i.clave
        response_data["estados"][cont]['abrev'] = i.abrev
        response_data["estados"][cont]['riskIndex'] = i.risk
        cont = cont + 1

    response_data['result'] = 'success'
    return JsonResponse(response_data, status = 200)
 else:
    response_data= {}
    response_data['result'] = 'error'
    respnse_data['message'] = 'Invalid Request'
    return JsonResponse(response_data, status = 403)

def movielogin(request):
    if request.method == 'POST':
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Metodo valido'
        return JsonResponse(response_data, status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Metodo invalido'
        return JsonResponse(response_data, status=403)

def movieclient(request):
        if request.method == 'POST':
            response_data = {}
            response_data['result'] = 'success'
            response_data['message'] = 'Metodo valido'
            return JsonResponse(response_data, status=200)
        else:
            response_data = {}
            response_data['result'] = 'error'
            response_data['message'] = 'Metodo invalido'
            return JsonResponse(response_data, status=403)
def login(request):
    #VALIDATE METHOD
    if request.method == 'POST':

        #DECLARE RESPONSE

        #CHECK JSON STRUCTURE

        if checkJson().isJson(request.body) == True:

            response_data = {}


            #CHECK JSON CONTENT
            json_data = json.loads(request.body)
            attr_error = False
            attrErrorMsg = ""

            if 'user' not in json_data:
                attr_error = True
                attrErrorMsg = "se requiere usuario"
            if 'password' not in json_data:
                attr_error = True
                attrErrorMsg = "se requiere contraseña"
            if attr_error == True:
                response_data['result'] = 'error'
                response_data['message'] = attrErrorMsg
                return JsonResponse(response_data, status=401)
            #CHECK IF USER EXITST
            try:

                #TAKE PASSWORD OF THE USER
                #CHECK IF PASSWORD IS CORRECT
                obj = ApiUsers.objects.get(user = json_data['user'])
                passCom = check_password(json_data['password'], obj.password)

                if passCom:
                    #CHECK IF USER HAS API-KEY
                    response_data['result'] ='success'
                    response_data['message'] =''

                    obj.api_key = ApiKey().generate_key_complex()
                    obj.save()

                    return JsonResponse(response_data, status = 200)

                else:
                    
                    response_data['result'] ='error'
                    response_data['message'] ='El usuario no existe o la contraseña es incorrecta'
                    return JsonResponse(response_data, status = 401)

                return JsonResponse(response_data, status= 200)

            except ApiUsers.DoesNotExist:
                response_data['result'] ='error'
                response_data['message'] ='El usuario no existe o la contraseña es incorrecta'
                return JsonResponse(response_data, status = 400)

            else:
                
                response_data['result'] = 'success'
                response_data['message'] = ''
                return JsonResponse(response_data, status=200)

            response_data['result'] = 'success'
            response_data['message'] = ''
            return JsonResponse(response_data, status=200)

        else:
            
            response_data = {}
            response_data['result'] = 'error'
            response_data['message'] = 'Invalid Json'
            return JsonResponse(response_data, status=400)

    else:
        responseData = {}
        responseData['result'] = 'error'
        responseData['message'] = 'Invalid Request'
        return JsonResponse(responseData, status=400)

def makepassword(request,password):
    hashPassword = make_password(password)
    response_data = {}
    response_data['password'] = hashPassword
    return JsonResponse(response_data, status=200)
