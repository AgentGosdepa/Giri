from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.auth.models import User
from .models import *
from .form import *

#*********************************************************************************
def index(request):
	if request.method == "POST":
		if ('find' in request.POST):
			name = request.POST.get("name")
			surname = request.POST.get("surname")
			patronymic = request.POST.get("patronymic")

			sportsmens = Sportsmen.objects.none()
			if not name == '':
				if not surname == '':
					if not patronymic == '':
						sportsmens = Sportsmen.objects.filter(name = name, surname = surname, patronymic = patronymic)
					else:
						sportsmens = Sportsmen.objects.filter(name = name, surname = surname)
				elif not patronymic == '':
					sportsmens = Sportsmen.objects.filter(name = name, patronymic = patronymic)
				else:
					sportsmens = Sportsmen.objects.filter(name = name)
			else:
				if not surname == '':
					if not patronymic == '':
						sportsmens = Sportsmen.objects.filter(surname = surname, patronymic = patronymic)
					else:
						sportsmens = Sportsmen.objects.filter(surname = surname)
				elif not patronymic == '':
					sportsmens = Sportsmen.objects.filter(patronymic = patronymic)
			
			results = Result.objects.none()
			for sportsmen in sportsmens:
				results |= Result.objects.filter(sportsmenid = sportsmen)
			return render(request, "index.html", {"sportsmens": sportsmens, "results": results})

		elif ('signin' in request.POST):
			login = request.POST.get("login")
			password = request.POST.get("password")

	else:
		return render(request, "index.html", {"sportsmens": Sportsmen.objects.all(), "results": Result.objects.all(), "isauth": request.session.get('isauth', False), "userid": request.session.get('userid', -1),"usertype": request.session.get('usertype', "U")})

#*********************************************************************************
def admin(request):
	isauth = request.session.get('isauth', False)
	userid = request.session.get('userid', -1)

	try:
		if not Users.objects.get(id = userid).permission == 'A':
			userid = -1
	except ObjectDoesNotExist:
		userid = -1

	if (not isauth or userid == -1):
		return HttpResponseRedirect("/")

	if request.method == "POST":
		if ('submit1' in request.POST):
			name = 					request.POST.get("name")
			surname = 				request.POST.get("surname")
			patronymic = 			request.POST.get("patronymic")
			region = 				request.POST.get("region")
			dateofbirth = 			request.POST.get("birthday")
			category = 				request.POST.get("category")

			sportsmen = Sportsmen.objects.create(name = name,
			surname = surname,
			patronymic = patronymic,
			region = region,
			dateofbirth = dateofbirth,
			category = category)
#********************************************	
		elif ('submit2' in request.POST):
			date =					request.POST.get("date")
			place = 				request.POST.get("place")
			status = 				request.POST.get("status")

			competition = Competition.objects.create(date = date, 
			place = place,
			status = status)	
#********************************************	
		elif ('submit3' in request.POST):
			judgename = 			request.POST.get("judgename")
			judgesurname = 			request.POST.get("judgesurname")
			judgepatronymic = 		request.POST.get("judgepatronymic")

			judge = Judge.objects.create(judgename = judgename,
			judgesurname = judgesurname,
			judgepatronymic = judgepatronymic)
#********************************************		
		elif ('submit4' in request.POST):
			sportsmenid = 			request.POST.get("sportsmenid")
			competitionid = 		request.POST.get("competitionid")
			judgeid = 				request.POST.get("judgeid")
			result = 				request.POST.get("result")
			mastername = 			request.POST.get("mastername")
			mastersurname = 		request.POST.get("mastersurname")
			masterpatronymic = 		request.POST.get("masterpatronymic")
			discipline = 			request.POST.get("discipline")

			result = Result.objects.create(sportsmenid = Sportsmen.objects.get(id = sportsmenid),
			competitionid = Competition.objects.get(id = competitionid),
			judgeid = Judge.objects.get(id = judgeid),
			result = result, 
			mastername = mastername,
			mastersurname = mastersurname, 
			masterpatronymic = masterpatronymic, 
			discipline = discipline,
			platform = 0)	
#********************************************		
		elif ('submit5' in request.POST):
			username = 					request.POST.get("username")
			password = 					request.POST.get("password")
			permission = 				request.POST.get("permission")
			judgeid = 					request.POST.get("judgeid")				

			user = Users.objects.create(username = username,
			password = password,
			permission = permission,
			judgeid = judgeid)	
#********************************************
		elif ('delete_sportsmen' in request.POST):
			Sportsmen.objects.get(id = request.POST.get("delete_sp")).delete()
#********************************************	
		elif ('delete_competition' in request.POST):
			Competition.objects.get(id = request.POST.get("delete_comp")).delete()
#********************************************	
		elif ('delete_judge' in request.POST):
			Judge.objects.get(id = request.POST.get("delete_jud")).delete()
#********************************************	
		elif ('delete_result' in request.POST):
			Result.objects.get(id = request.POST.get("delete_res")).delete()
#********************************************	
		elif ('delete_user' in request.POST):
			Users.objects.get(id = request.POST.get("delete_use")).delete()
#********************************************	
	return render(request, "admin.html", {"sportsmens": Sportsmen.objects.all(),
		"competitions": Competition.objects.all(), "judges": Judge.objects.all(),
		"results": Result.objects.all(), "users": Users.objects.all(), 
		"isauth": request.session.get('isauth', True), 
		"userid": request.session.get('userid', -1)})
    
#********************************************************************************* 
def operator(request):
	isauth = request.session.get('isauth', False)
	userid = request.session.get('userid', -1)

	try:
		if not Users.objects.get(id = userid).permission == 'O':
			userid = -1
	except ObjectDoesNotExist:
		userid = -1

	if (not isauth or userid == -1):
		return HttpResponseRedirect("/")

	if request.method == "POST":
		if ('submit1' in request.POST):
			name = 					request.POST.get("name")
			surname = 				request.POST.get("surname")
			patronymic = 			request.POST.get("patronymic")
			region = 				request.POST.get("region")
			dateofbirth = 			request.POST.get("birthday")
			category = 				request.POST.get("category")

			sportsmen = Sportsmen.objects.create(name = name,
			surname = surname,
			patronymic = patronymic,
			region = region,
			dateofbirth = dateofbirth,
			category = category)
#********************************************	
		elif ('submit2' in request.POST):
			date =					request.POST.get("date")
			place = 				request.POST.get("place")
			status = 				request.POST.get("status")

			competition = Competition.objects.create(date = date, 
			place = place,
			status = status)
#********************************************	
		elif ('submit3' in request.POST):
			judgename = 			request.POST.get("judgename")
			judgesurname = 			request.POST.get("judgesurname")
			judgepatronymic = 		request.POST.get("judgepatronymic")

			judge = Judge.objects.create(judgename = judgename,
			judgesurname = judgesurname,
			judgepatronymic = judgepatronymic)
#********************************************		
		elif ('submit4' in request.POST):
			sportsmenid = 			request.POST.get("sportsmenid")
			competitionid = 		request.POST.get("competitionid")
			judgeid = 				request.POST.get("judgeid")
			result = 0				#request.POST.get("result")
			mastername = 			request.POST.get("mastername")
			mastersurname = 		request.POST.get("mastersurname")
			masterpatronymic = 		request.POST.get("masterpatronymic")
			discipline = 			request.POST.get("discipline")
			platform = 				request.POST.get("platform")

			result = Result.objects.create(sportsmenid = Sportsmen.objects.get(id = sportsmenid),
			competitionid = Competition.objects.get(id = competitionid),
			judgeid = Judge.objects.get(id = judgeid),
			result = result, 
			mastername = mastername,
			mastersurname = mastersurname, 
			masterpatronymic = masterpatronymic, 
			discipline = discipline,
			platform = platform)
#********************************************
		elif ('delete_sportsmen' in request.POST):
			Sportsmen.objects.get(id = request.POST.get("delete_sp")).delete()
#********************************************	
		elif ('delete_competition' in request.POST):
			Competition.objects.get(id = request.POST.get("delete_comp")).delete()
#********************************************	
		elif ('delete_judge' in request.POST):
			Judge.objects.get(id = request.POST.get("delete_jud")).delete()
#********************************************	
		elif ('delete_result' in request.POST):
			Result.objects.get(id = request.POST.get("delete_res")).delete()
#********************************************	
	return render(request, "operator.html", {"sportsmens": Sportsmen.objects.all(),
		"competitions": Competition.objects.all(), "judges": Judge.objects.all(),
		"results": Result.objects.all(), 
		"isauth": request.session.get('isauth', True), 
		"userid": request.session.get('userid', -1)})

#*********************************************************************************
def judge(request):
	isauth = request.session.get('isauth', False)
	userid = request.session.get('userid', -1)

	try:
		if not Users.objects.get(id = userid).permission == 'J':
			userid = -1
	except ObjectDoesNotExist:
		userid = -1

	if (not isauth or userid == -1):
		return HttpResponseRedirect("/")

	if request.method == "POST":	
		if ('submit4' in request.POST):
			sportsmenid = 			request.POST.get("sportsmenid")
			competitionid = 		request.POST.get("competitionid")
			judgeid = 				Users.objects.get(id = request.session.get('userid')).judgeid
			results = 				request.POST.get("result")
			#mastername = 			request.POST.get("mastername")
			#mastersurname = 		request.POST.get("mastersurname")
			#masterpatronymic = 		request.POST.get("masterpatronymic")
			#discipline = 			request.POST.get("discipline")
			#platform = 				request.POST.get("platform")

			try:
				result = Result.objects.get(sportsmenid = Sportsmen.objects.get(id = sportsmenid),
				competitionid = Competition.objects.get(id = competitionid),
				judgeid = Judge.objects.get(id = judgeid))
				result.result = results
				result.save()
			except ObjectDoesNotExist:
				return HttpResponseRedirect("/judge/")

#********************************************	
		elif ('delete_result' in request.POST):
			Result.objects.get(id = request.POST.get("delete_res")).delete()			

	
	return render(request, "judge.html", {"sportsmens": Sportsmen.objects.all(),
		"competitions": Competition.objects.all(), "judges": Judge.objects.all(),
		"results": Result.objects.filter(judgeid = Judge.objects.get(id = Users.objects.get(id = request.session.get('userid', -1)).judgeid)), 
		"isauth": request.session.get('isauth', True), 
		"userid": request.session.get('userid', -1)})

def dashboard_get(request):
	if request.method == "GET":
		platform_id = request.GET.get("platform")
		competition_id = request.GET.get("competition")

		try:
			results = Result.objects.filter(platform = platform_id, competitionid = competition_id)
			sportsmen = dict()
			for result in results:
				sportsmen[str(result.sportsmenid.id)] = result.sportsmenid.name + " " + result.sportsmenid.surname + " " + result.sportsmenid.patronymic
			
			answer = HttpResponse()
			answer.write(sportsmen)
			return answer

		except ObjectDoesNotExist:
			return HttpResponse("Not found")			
	else:
		return HttpResponse("GET REQUEST REQUIRED!")

def dashboard_set(request):
	if request.method == "GET":
		sportsmen_id = request.GET.get("sportsmenid")
		competition_id = request.GET.get("competition")
		result_count = request.GET.get("result")

		try:
			result = Result.objects.get(sportsmenid = sportsmen_id, competitionid = competition_id)
			result.result = result_count
			result.save()
			return HttpResponse("ADDED!")
		except ObjectDoesNotExist:
			return HttpResponse("NOT FOUND!")
	else:
		return HttpResponse("GET REQUEST REQUIRED!")

# Login form page
def login(request):
	return render(request, "login.html")

def log(request):
	try:
		m = Users.objects.get(username=request.POST['username'])
		if m.password == request.POST['password']:
			request.session['isauth'] = True
			request.session['userid'] = m.id
			request.session['usertype'] = m.permission
			return HttpResponseRedirect("/")
		else:
			return HttpResponse("Неверный пароль!")
	except ObjectDoesNotExist:
		return HttpResponse("Неверный логин!")

def logout(request):
	try:
		if 'isauth' in request.session:
			del request.session['isauth']
		if 'userid' in request.session:
			del request.session['userid']
		if 'usertype' in request.session:
			del request.session['usertype']			
	except KeyError:
		pass
	return HttpResponseRedirect("/")

# Profile form page
def profile(request):
	return render(request, "profile.html", {"results": Result.objects.all(),
	"competitions": Competition.objects.all()})