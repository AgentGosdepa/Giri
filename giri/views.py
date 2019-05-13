from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from .models import *
from .form import *

#*********************************************************************************
def index(request):
	if request.method == "POST":
		if ('find' in request.POST):
			nsp = request.POST.get("nsp")
			name = str()
			surname = str()
			patronymic = str()

			flag = 0
			for i in nsp:
				if (i == ' '):
					flag += 1
					continue
				if flag == 0:
					name += i
				if flag == 0:
					surname += i
				if flag == 0:
					patronymic += i				

			sportsmens = Sportsmen.objects.filter(name = name, surname = surname, patronymic = patronymic)
			results = Result.objects.none()

			for sportsmen in sportsmens:
				results |= Result.objects.filter(sportsmenid = sportsmen)
			return render(request, "index.html", {"sportsmens": sportsmens, "results": results})

		elif ('signin' in request.POST):
			login = request.POST.get("login")
			password = request.POST.get("password")

	else:
		return render(request, "index.html", {"sportsmens": Sportsmen.objects.all(), "results": Result.objects.all()})

#*********************************************************************************
def admin(request):
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

			competition = Compitition.objects.create(date = date, 
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
			competitionid = Compitition.objects.get(id = competitionid),
			judgeid = Judge.objects.get(id = judgeid),
			result = result, 
			mastername = mastername,
			mastersurname = mastersurname, 
			masterpatronymic = masterpatronymic, 
			discipline = discipline,
			platform = 0)	
#********************************************
		elif ('delete_sportsmen' in request.POST):
			Sportsmen.objects.get(id = request.POST.get("delete_sp")).delete()
#********************************************	
		elif ('delete_competition' in request.POST):
			Compitition.objects.get(id = request.POST.get("delete_comp")).delete()
#********************************************	
		elif ('delete_judge' in request.POST):
			Judge.objects.get(id = request.POST.get("delete_jud")).delete()
#********************************************	
		elif ('delete_result' in request.POST):
			Result.objects.get(id = request.POST.get("delete_res")).delete()
#********************************************	
		return render(request, "admin.html", {"sportsmens": Sportsmen.objects.all(),
			"competitions": Compitition.objects.all(), "judges": Judge.objects.all(),
			"results": Result.objects.all()})
	else:
		return render(request, "admin.html", {"sportsmens": Sportsmen.objects.all(),
			"competitions": Compitition.objects.all(), "judges": Judge.objects.all(),
			"results": Result.objects.all()})
    

#********************************************************************************* 
def operator(request):
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

			competition = Compitition.objects.create(date = date, 
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
			#result = 				request.POST.get("result")
			result = 				0
			mastername = 			request.POST.get("mastername")
			mastersurname = 		request.POST.get("mastersurname")
			masterpatronymic = 		request.POST.get("masterpatronymic")
			discipline = 			request.POST.get("discipline")

			result = Result.objects.create(sportsmenid = Sportsmen.objects.get(id = sportsmenid),
			competitionid = Compitition.objects.get(id = competitionid),
			judgeid = Judge.objects.get(id = judgeid),
			result = result, 
			mastername = mastername,
			mastersurname = mastersurname, 
			masterpatronymic = masterpatronymic, 
			discipline = discipline)			
#********************************************	
		return render(request, "operator.html", {"sportsmens": Sportsmen.objects.all(),
			"competitions": Compitition.objects.all(), "judges": Judge.objects.all(),
			"results": Result.objects.all()})
	else:
		return render(request, "operator.html", {"sportsmens": Sportsmen.objects.all(),
			"competitions": Compitition.objects.all(), "judges": Judge.objects.all(),
			"results": Result.objects.all()})

#*********************************************************************************
def judge(request):
    return render(request, "judge.html")

def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
            
			return HttpResponseRedirect("/")
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
		return render(request, 'contact.html', {'form': form})


def sportsmens(request):
	if request.method == "POST":
		if ('submit1' in request.POST):
			name = 					request.POST.get("name")
			surname = 				request.POST.get("surname")			
			patronymic = 			request.POST.get("patronymic")
			region = 				request.POST.get("region")
			dateofbirth = 			request.POST.get("birthday")
			category = 				request.POST.get("category")

			sportsmen = Sportsmen.objects.create(name = name,
			surname = surname,			patronymic = patronymic,
			region = region,
			dateofbirth = dateofbirth,
			category = category)

		elif ('delete_sportsmen' in request.POST):
			Sportsmen.objects.get(id = request.POST.get("delete_sp")).delete()

	return render(request, 'sportsmens.html', {"sportsmens": Sportsmen.objects.all()})

def competitions(request):
	if request.method == "POST":
		if ('submit2' in request.POST):
			date =					request.POST.get("date")
			place = 				request.POST.get("place")
			status = 				request.POST.get("status")

			competition = Compitition.objects.create(date = date, 
			place = place,
			status = status)

		elif ('delete_competition' in request.POST):
			Compitition.objects.get(id = request.POST.get("delete_comp")).delete()
						
	return render(request, 'competitions.html', {"competitions": Competition.objects.all()})

def judges(request):
	if request.method == "POST":
		if ('submit3' in request.POST):
			judgename = 			request.POST.get("judgename")
			judgesurname = 			request.POST.get("judgesurname")
			judgepatronymic = 		request.POST.get("judgepatronymic")

			judge = Judge.objects.create(judgename = judgename,
			judgesurname = judgesurname,
			judgepatronymic = judgepatronymic)

		elif ('delete_judge' in request.POST):
			Judge.objects.get(id = request.POST.get("delete_jud")).delete()

	return render(request, 'judges.html', {"judges": Judge.objects.all()})

def sj(request):	
	pass


def adduser(request):
	pass

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

