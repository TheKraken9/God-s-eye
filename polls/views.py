import json

import folium
from django.core.serializers import serialize

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from hole import hole_description
from polls import models
from polls.models import MadagascarRoad as mada
from polls.models import Routes
from polls.models import Route_fusion
from polls.models import Holedescription
from polls.models import Holeintern
from polls.models import Hospital
from polls.models import Environment
from polls.models import Description
# from django.core.serializers import serialize
from django.contrib.gis.serializers import geojson
from django.contrib.gis.serializers.geojson import Serializer
from django.contrib.gis.geos import Point, Polygon, LinearRing, MultiLineString


# Create your views here.

def index(request):
    return render(request, 'index.html')


def detail(request):
    if request.method == 'POST':
        condition = request.POST.get('rn', '')
        rd = hole_description.allSpecifiedRoad(condition)
        rn = hole_description.specified(condition)
        all_result_list = []
        result_list = []
        for rw in rd:
            result_specified = []
            for cols in rw:
                result_specified.append(cols)
            all_result_list.append(result_specified)
        for row in rn:
            result_row = []
            for col in row:
                result_row.append(col)
            result_list.append(result_row)
        route = Route_fusion.objects.all()
        holedesc = Holedescription.objects.all()
        holeintern = Holeintern.objects.all()
        environment = Environment.objects.all()
        desc = Description.objects.all()
        my_geojson = serialize('geojson', route)
        my_holedesc = serialize('geojson', holedesc)
        my_holeintern = serialize('geojson', holeintern)
        my_environment = serialize('geojson', environment)
        print(my_environment)
        context = {'my_environment': my_environment, 'allnationalroute': all_result_list, 'nationalroute': result_list, 'my_geojson': my_geojson, 'my_holedesc': my_holedesc, 'my_holeintern': my_holeintern, 'desc': list(desc)}
        return render(request, 'map.html', context)
    else:
        return render(request, 'index.html')


def routes(request):
    with open('output.json') as f:
        geojson_data = json.load(f)
    response = HttpResponse(json.dumps(geojson_data), content_type='application/json',
                            headers={'Content-Disposition': 'inline'})
    return response


def which_road(request):
    if request.method == 'POST':
        condition = request.POST.get('road', '')
        my_geo = Route_fusion.objects.filter(startdesc=condition)
        my_geojson = serialize('geojson', my_geo)
        holedesc = hole_description.cost(condition)
        context = {'prices': holedesc, 'my_geojson': my_geojson, 'startdesc': condition}
        return render(request, 'searchmap.html', context)


def all_which_road(request):
    if request.method == 'POST':
        condition = request.POST.get('road', '')
        my_geo = Route_fusion.objects.filter(roadno=condition)
        holes = Holedescription.objects.filter(idroad=condition)
        holepoint = Holeintern.objects.filter(idhole=1)
        hole_geojson = serialize('geojson', holes)
        my_geojson = serialize('geojson', my_geo)
        point_geojson = serialize('geojson', holepoint)
        holedesc = hole_description.all_cost(condition)
        context = {'prices': holedesc, 'my_geojson': my_geojson, 'startdesc': condition, 'hole_geojson': hole_geojson, 'point_geojson': point_geojson}
        return render(request, 'searchmap.html', context)


def all_all_which_road(request):
    if request.method == 'POST':
        condition = request.POST.get('road', '')
        if condition == 'RNP 6s' or condition == 'RNP 6n':
            condition = 'RNP 6'
        my_geo = Route_fusion.objects.filter(roadno__icontains=condition)
        my_geojson = serialize('geojson', my_geo)
        holedesc = hole_description.all_cost(condition)
        context = {'prices': holedesc, 'my_geojson': my_geojson, 'startdesc': condition}
        return render(request, 'searchmap.html', context)


def request(request):
    if request.method == 'POST':
        req = request.POST.get('request', '')
        my_geo = hole_description.execute_request(req)
        # my_geo = Routes.objects.raw(req)
        holedesc = hole_description.my_cost(req)
        # my_geojson = serialize('geojson', my_geo)
        my_geojson = my_geo
        context = {'prices': holedesc, 'my_geojson': my_geojson, 'startdesc': req}
        return render(request, 'searchmap.html', context)


def route_request(request):
    if request.method == 'POST':
        road = request.POST.get('road')
        start = request.POST.get('start_km')
        end = request.POST.get('end_km')
        condition = "" + road + " pk" + start + " vers pk" + end
        my_geo = Route_fusion.objects.filter(roadno=road, start_km__gte=start, end_km__lte=end)
        print(my_geo)
        my_geojson = serialize('geojson', my_geo)
        holedesc = hole_description.my_cost(
            "select * from holedescri where nationalroute='{}' and pkbegin >= {} and pkend <= {}".format(road, start,
                                                                                                         end))
        context = {'my_geojson': my_geojson, 'prices': holedesc, 'startdesc': condition}
        return render(request, 'searchmap.html', context)


def route_requests(request):
    if request.method == 'POST':
        start = request.POST.get('start_km')
        end = request.POST.get('end_km')
        condition = "pk" + start + " vers pk" + end
        my_geo = Route_fusion.objects.filter(start_km__gte=start, end_km__lte=end)
        print(my_geo)
        my_geojson = serialize('geojson', my_geo)
        holedesc = hole_description.my_cost(
            "select * from holedescri where pkbegin >= {} and pkend <= {}".format(start, end))
        context = {'my_geojson': my_geojson, 'prices': holedesc, 'startdesc': condition}
        return render(request, 'searchmap.html', context)


def result(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        condition = request.POST.get('road', '')
        my_geo = Route_fusion.objects.filter(roadno=condition)
        holes = Holedescription.objects.filter(idroad=condition)
        hole_geojson = serialize('geojson', holes)
        my_geojson = serialize('geojson', my_geo)
        res = Hospital.objects.raw("SELECT h.gid as gid, h.name as name, ST_AsGeoJSON(h.geom) as geom FROM hospital h CROSS JOIN holeintern p WHERE st_distanceSphere(st_setsrid(h.geom, 4326), st_setsrid(st_makepoint(st_x(p.geom), st_y(p.geom)), 4326)) <= {}".format(pk))
        print(res)
        result_geojson = serialize('geojson', res, geometry_field='3')
        print(result_geojson)
        context = {'result_geojson': result_geojson, 'my_geojson': my_geojson, 'startdesc': condition, 'hole_geojson': hole_geojson}
        return render(request, 'result.html', context)


def descri(request):
    if request.method == 'POST':
        desc = request.POST.get('descri')
        RNs = hole_description.getAllRn()
        print(RNs)
        allRN = [rn[0] for rn in RNs]
        priority = list()
        count = 0
        nb = 0
        for rn in allRN:
            print(rn)
            these_rn = hole_description.getHoleDescription(rn)
            for this_rn in these_rn:
                geoms = hole_description.getGeomHoleDescription(this_rn)
                for geom in geoms:
                    nb += hole_description.getCalcul(geom, desc)
                nb += hole_description.getGeomInternalHoleDescription(this_rn)
                if count < nb:
                    count = nb
                    priority = rn

        return priority

