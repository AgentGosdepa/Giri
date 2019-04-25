from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import *

#*********************************************************************************
def index(request):
	if request.method == "POST":
		name = request.POST.get("name")
		surname = request.POST.get("surname")
		patronymic = request.POST.get("patronymic")
		sportsmens = Sportsmen.objects.filter(name = name, surname = surname, patronymic = patronymic)
		results = Result.objects.none()

		for sportsmen in sportsmens:
			results = Result.objects.filter(sportsmenid = sportsmen)

		return render(request, "index.html", {"sportsmens": sportsmens, "results": results})
	else:
		return render(request, "index.html")

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
			discipline = discipline)	
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

