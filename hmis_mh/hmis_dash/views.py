import json
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core import serializers
from django.core.serializers import serialize
from django.db.models import Q
from dashboard.models import MhAreaDetails, MhDSdPw, MhDSdCi, MhDSdCd
from django.core.serializers.json import DjangoJSONEncoder 
from django.db.models import F
from .models import (MhDSdPwPie, MhDSdCdPie, MhDSdCiPie, MhDtGeojson)

# Create your views here.

class HMISDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dash_base.html"
    

class hmisBarChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
        else:    
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
        
        return render(request,'hmis_dash/barchart.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class hmisLineChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 

        if district == '405': 
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & (Q(area_parent_id=22))).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/linechart.html', {'data':jsondata, 'fy': fy_name, 'area_list': area_list, 'dist_name': district})


class fyLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy)
        if district == '405': 
            data = list(MhDSdPw.objects.filter(Q(area_parent_id=405)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdPw.objects.filter(Q(area_parent_id=22)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        
        fyList = MhDSdPw.objects.values('financial_year').distinct().order_by('financial_year').exclude(financial_year='2021-2022')
        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
        return render(request,'hmis_dash/fy_line.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'area_list': area_list})


class fyLineNum(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy)
        if district == '405': 
            data = list(MhDSdPw.objects.filter( Q(area_parent_id=405)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdPw.objects.filter( Q(area_parent_id=22)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])
        fyList = MhDSdPw.objects.values('financial_year').distinct().order_by('financial_year').exclude(financial_year='2021-2022')
        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/fy_lineNum.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'area_list': area_list})


class hmisBarNumericChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            
        else:    
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
 
        
        return render(request,'hmis_dash/barNumericChart.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class hmisLineNumericChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 

        if district == '405': 
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & (Q(area_parent_id=22))).exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/lineNumericChart.html', {'data':jsondata, 'fy': fy_name, 'area_list':area_list, 'dist_name': district})


class chldImmuBar(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            
        else:    
            data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
        
        return render(request,'hmis_dash/chldImmuBar.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldImmuLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 

        if district == '405': 
            data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & (Q(area_parent_id=22))).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)


        return render(request,'hmis_dash/chldImmuLine.html', {'data':jsondata, 'fy': fy_name, 'area_list': area_list, 'dist_name': district})


class chldImmuBarNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            
        else:    
            data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
        
        return render(request,'hmis_dash/chldImmuBarNumeric.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldImmuLineNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 

        if district == '405': 
            data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & (Q(area_parent_id=22))).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)


        return render(request,'hmis_dash/chldImmuLineNumeric.html', {'data':jsondata, 'fy': fy_name, 'area_list': area_list, 'dist_name': district})


class chldDiseaseBar(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            
        else:    
            data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
        
        return render(request,'hmis_dash/chldDiseaseBar.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldDiseaseLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 

        if district == '405': 
            data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & (Q(area_parent_id=22))).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/chldDiseaseLine.html', {'data':jsondata, 'fy': fy_name, 'area_list':area_list, 'dist_name': district})


class chldDiseaseBarNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            
        else:    
            data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
        
        return render(request,'hmis_dash/chldDiseaseBarNumeric.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldDiseaseLineNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 

        if district == '405': 
            data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & (Q(area_parent_id=22))).exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])
        print(area_list)

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/chldDiseaseLineNumeric.html', {'data':jsondata, 'fy': fy_name, 'area_list':area_list,'dist_name': district})

    
class hmisTableChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            pw_data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            childIm_data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            childDi_data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
        else:
            pw_data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())
            childIm_data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())
            childDi_data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in pw_data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        for i in childIm_data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])   

        for i in childDi_data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])  

        json_childIm_data = json.dumps(childIm_data, cls=DjangoJSONEncoder)
        json_childDi_data = json.dumps(childDi_data, cls=DjangoJSONEncoder)
        jsonpw_data = json.dumps(pw_data, cls=DjangoJSONEncoder)

        context = {
            'chilIm_data': json_childIm_data,
            'childDi_data': json_childDi_data,
            'pw_data': jsonpw_data
        }

        return render(request,'hmis_dash/tableOverview.html', {'context':context, 'fy': fy_name, 'dist_name': district})


class pieStateLevel(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdPwPie.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            
        else:    
            data = list(MhDSdPwPie.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/piechart_stlvl.html', {'data':jsondata, 'fy': fy_name, 'dist_name':district})


class pieChildImmu(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdCiPie.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            
        else:    
            data = list(MhDSdCiPie.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/pieChldImmu.html', {'data':jsondata, 'fy': fy_name, 'dist_name':district})


class pieChildDisease(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdCiPie.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            
        else:    
            data = list(MhDSdCiPie.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/pieChldDisease.html', {'data':jsondata, 'fy': fy_name, 'dist_name':district})


class mapStPW(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        st_data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        dt_data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())

        for i in st_data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        for i in dt_data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])            
        
        st_jsondata = json.dumps(st_data, cls=DjangoJSONEncoder)

        dt_jsondata = json.dumps(dt_data, cls=DjangoJSONEncoder)
        
        st_geodata = serialize('geojson', GeojsonIndiaLevel.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state', 'area_id'))

        dt_geodata = serialize('geojson', MhDtGeojson.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state', 'district', 'area_id'))                                
        
        context = {
            'st_data': st_jsondata,
            'dt_data': dt_jsondata,
            'st_geodata': st_geodata,
            'dt_geodata': dt_geodata
        }

        return render(request,'hmis_dash/mapPW.html', {'context':context, 'fy': fy_name})


class mapStChldImmu(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        st_data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        dt_data = list(MhDSdCi.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())

        for i in st_data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        for i in dt_data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])            
        
        st_jsondata = json.dumps(st_data, cls=DjangoJSONEncoder)

        dt_jsondata = json.dumps(dt_data, cls=DjangoJSONEncoder)
        
        st_geodata = serialize('geojson', GeojsonIndiaLevel.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state', 'area_id'))

        dt_geodata = serialize('geojson', MhDtGeojson.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state', 'district', 'area_id'))                                
        
        context = {
            'st_data': st_jsondata,
            'dt_data': dt_jsondata,
            'st_geodata': st_geodata,
            'dt_geodata': dt_geodata
        }


        return render(request,'hmis_dash/mapChldImmu.html', {'context':context, 'fy': fy_name})


class mapStChldDisease(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        st_data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        dt_data = list(MhDSdCd.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())

        for i in st_data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        for i in dt_data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])            
        
        st_jsondata = json.dumps(st_data, cls=DjangoJSONEncoder)

        dt_jsondata = json.dumps(dt_data, cls=DjangoJSONEncoder)
        
        st_geodata = serialize('geojson', GeojsonIndiaLevel.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state', 'area_id'))

        dt_geodata = serialize('geojson', MhDtGeojson.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state', 'district', 'area_id'))                                
        
        context = {
            'st_data': st_jsondata,
            'dt_data': dt_jsondata,
            'st_geodata': st_geodata,
            'dt_geodata': dt_geodata
        }


        return render(request,'hmis_dash/mapChldDisease.html', {'context':context, 'fy': fy_name})


class fyChldImmuLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy)
        if district == '405': 
            data = list(MhDSdCi.objects.filter( Q(area_parent_id=405)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdCi.objects.filter( Q(area_parent_id=22)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])
        fyList = MhDSdCi.objects.values('financial_year').distinct().order_by('financial_year').exclude(financial_year='2021-2022')
        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/fy_ci_line.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'area_list': area_list})



class fyChldImmuLineNum(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy)
        if district == '405': 
            data = list(MhDSdCi.objects.filter( Q(area_parent_id=405)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdCi.objects.filter( Q(area_parent_id=22)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])
        fyList = MhDSdCi.objects.values('financial_year').distinct().order_by('financial_year').exclude(financial_year='2021-2022')
        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/fy_ci_lineNum.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'area_list': area_list})


class fyChldDiseaseLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy)
        if district == '405': 
            data = list(MhDSdCd.objects.filter( Q(area_parent_id=405)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdCd.objects.filter( Q(area_parent_id=22)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])
        fyList = MhDSdCd.objects.values('financial_year').distinct().order_by('financial_year').exclude(financial_year='2021-2022')
        jsondata = json.dumps(data, cls=DjangoJSONEncoder)

        return render(request,'hmis_dash/fy_cd_line.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'area_list': area_list})


class fyChldDiseaseLineNum(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy)
        if district == '405': 
            data = list(MhDSdCd.objects.filter( Q(area_parent_id=405)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=405)).values('area_name', 'area_id').distinct().order_by('area_id')
            
        else:    
            data = list(MhDSdCd.objects.filter( Q(area_parent_id=22)).order_by('month').exclude(month='All').values())
            area_list = MhAreaDetails.objects.filter(Q(area_parent_id=22)).values('area_name', 'area_id').distinct().order_by('area_id')

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])
            
        fyList = MhDSdCd.objects.values('financial_year').distinct().order_by('financial_year').exclude(financial_year='2021-2022')
        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
        return render(request,'hmis_dash/fy_cd_lineNum.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'area_list': area_list})


class CompBarPw(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            
        else:    
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
        
        return render(request,'hmis_dash/compBarPW.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})        


class CompBarPwNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        if district == '405': 
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=405)).values())
            
        else:    
            data = list(MhDSdPw.objects.filter(Q(financial_year=fy_name) & Q(area_parent_id=22)).values())

        for i in data:
            area_n = MhAreaDetails.objects.filter(Q(area_id = i['area_id'])).values('area_name')
            i.update(area_n[0])

        jsondata = json.dumps(data, cls=DjangoJSONEncoder)
        
        return render(request,'hmis_dash/compBarPWNumeric.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})                
