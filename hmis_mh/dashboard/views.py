from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import (MhAreaDetails, MhDSdPw, MhDSdCd, MhDSdCi)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.serializers import serialize
from .serializers import HmisPwSerializer, HmisCdSerializer, HmisCiSerializer
import json
from django.http import JsonResponse

# Create your views here.


def create_post_area(request, fy=None, dist_name=None):
    dist = request.GET.get('dist_name', dist_name) 
    areaSelected = request.GET.get('area')
    dtSelected = request.GET.get('area_district')
    monthSelected = request.GET.get('month')
    fy_name = request.GET.get('fy', fy) 

    if ((areaSelected == '405') and (dtSelected != '0') ):
        pw_data = MhDSdPw.objects.filter(Q(area_id=dtSelected) & Q(financial_year=fy_name) & Q(month=monthSelected))
    else:
        pw_data = MhDSdPw.objects.filter(Q(area_id=areaSelected) & Q(financial_year=fy_name) & Q(month=monthSelected))

    ci_data = MhDSdCi.objects.filter(Q(area_id=areaSelected) & Q(financial_year=fy_name) & Q(month=monthSelected))
    cd_data = MhDSdCd.objects.filter(Q(area_id=areaSelected) & Q(financial_year=fy_name) & Q(month=monthSelected))

    pw_json = json.dumps(HmisPwSerializer(pw_data,  many=True).data)

    ci_json = json.dumps(HmisCiSerializer(ci_data,  many=True).data)
    cd_json = json.dumps(HmisCdSerializer(cd_data,  many=True).data)
    context = {
        'pw_data':pw_json,
        'ci_data':ci_json,
        'cd_data':cd_json
    }

    return JsonResponse({'context':context, 'dist_name': areaSelected})


class DashboardView(TemplateView):
    def get(self,request):
       
        return render(request,'dashboard/dash.html')


class RegionOverview(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    def post(self,request):
        username = request.user.username
        fy_name = request.POST['fy_select']
      
        area_name = 1
        pw_data = MhDSdPw.objects.filter(Q(area_id=405) & Q(financial_year=fy_name) & Q(month='All'))
        print(pw_data)
        ci_data = MhDSdCi.objects.filter(Q(area_id=405) & Q(financial_year=fy_name) & Q(month='All'))
        cd_data = MhDSdCd.objects.filter(Q(area_id=405) & Q(financial_year=fy_name) & Q(month='All'))

        st_name = MhAreaDetails.objects.filter(Q(area_level = 3)).values('area_name', 'area_id').distinct().order_by('area_id')
        dt_name = MhAreaDetails.objects.filter(Q(area_parent_id = 405)).values('area_name', 'area_id').distinct().order_by('area_id')

        month_name = MhDSdPw.objects.filter(Q(financial_year=fy_name)).values('month').distinct().order_by('month')

        pw_json = serializers.serialize('json',pw_data)
        print(pw_json)
        ci_json = serializers.serialize('json',ci_data)
        cd_json = serializers.serialize('json',cd_data)
        context = {
            'pw_data':pw_json,
            'ci_data':ci_json,
            'cd_data':cd_json
        }
        
        return render(request,'dashboard/dt_dashboard.html', {'st_list':st_name, 'dt_list':dt_name ,'dist_name':area_name, 'context':context, 'months':month_name, 'fy': fy_name})



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "dashboard/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")