from django.shortcuts import render
from django.views.generic import View
from .models import Company
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'chartjs/index.html')


class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format = None):
		xValues = []
		label = []
		company1_rank = []
		company2_rank = []
		company3_rank = []
		company4_rank = []
		company5_rank = []

		queryset = Company.objects.all()
		for item in queryset:
			xValues.append(item.date)
			label.append(item.symbol)
			if item.symbol == 'APPLONGC.NS':
				company1_rank.append(item.rank)
			
			elif item.symbol == 'CIPLA.NS':
				company2_rank.append(item.rank)

			elif item.symbol == 'COALINDIA.NS':
				company3_rank.append(item.rank)

			elif item.symbol == 'HEROMOTOCO.NS':
				company4_rank.append(item.rank)

			elif item.symbol == 'RELIANCE.NS':
				company5_rank.append(item.rank)

		
		xValues = list(set(xValues))
		# for datestring in xValues:
		def sortDates(datestring):
			datestring = str(datestring)
			split_up = datestring.split("-")
			return split_up

		xValues.sort(key=sortDates)
		# print(xValues)

		label = list(set(label))
		label.sort()
		# print(label)
		data = {
			"dates":xValues,
			"label":label,
			"rank1":company1_rank,
			"rank2":company2_rank,
			"rank3":company3_rank,
			"rank4":company4_rank,
			"rank5":company5_rank,
		}
		return Response(data)