from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point


# Create your models here.

class Route_fusion(models.Model):
    roadno = models.CharField(primary_key=True, max_length=20)
    start_km = models.FloatField()
    end_km = models.FloatField()
    longueur = models.FloatField()
    largeur = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)

    class Meta:
        db_table = 'route_fusion'


class Holedescription(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    idroad = models.CharField(max_length=20)
    pkbegin = models.IntegerField()
    pkend = models.IntegerField()
    width = models.IntegerField()
    holelevel = models.IntegerField()
    geom = gis_models.MultiLineStringField(srid=4326)

    class Meta:
        db_table = 'holedescription'


class Holelevel(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.IntegerField()
    thickness = models.IntegerField()

    class Meta:
        db_table = 'holelevel'


class Nationalroute(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    beginroute = models.CharField(max_length=50)
    endroute = models.CharField(max_length=50)
    beginpk = models.IntegerField()
    endpk = models.IntegerField()

    class Meta:
        db_table = 'nationalroute'


class Workmanship(models.Model):
    id = models.IntegerField(primary_key=True)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    duration = models.FloatField()

    class Meta:
        db_table = 'workmanship'


class MadagascarRoad(models.Model):
    id = models.IntegerField(primary_key=True)
    linkno = models.CharField(max_length=20)
    roadno = models.CharField(max_length=20)
    start_km = models.BigIntegerField()
    end_km = models.BigIntegerField()
    lenghtkm = models.FloatField()
    startdesc = models.CharField(max_length=100)
    enddesc = models.CharField(max_length=100)
    classe = models.CharField(max_length=50, db_column='class', default="")
    regions = models.CharField(max_length=50)
    width = models.FloatField()
    lanes = models.IntegerField()
    surftype = models.CharField(max_length=30)
    condition = models.CharField(max_length=30)
    aadt = models.BigIntegerField()
    iso3 = models.CharField(max_length=50)
    aicd_reg = models.IntegerField()
    p082806 = models.IntegerField()
    p073689 = models.IntegerField()

    class Meta:
        db_table = 'madagascarroad'


class Routes(models.Model):
    gid = models.IntegerField(primary_key=True)
    linkno = models.CharField(max_length=20)
    roadno = models.CharField(max_length=20)
    start_km = models.FloatField()
    end_km = models.FloatField()
    lengthkm = models.FloatField()
    startdesc = models.CharField(max_length=100)
    enddesc = models.CharField(max_length=100)
    classe = models.CharField(max_length=50, db_column='class', default="")
    regions = models.CharField(max_length=50)
    width = models.FloatField()
    lanes = models.IntegerField()
    surftype = models.CharField(max_length=30)
    condition = models.CharField(max_length=30)
    aadt = models.FloatField()
    iso3 = models.CharField(max_length=50)
    aicd_reg = models.IntegerField()
    p082806 = models.IntegerField()
    p073689 = models.IntegerField()
    geom = models.MultiLineStringField(srid=4326)

    class Meta:
        db_table = 'routes'


class Route_fusion(models.Model):
    roadno = models.CharField(primary_key=True, max_length=20)
    start_km = models.FloatField()
    end_km = models.FloatField()
    longueur = models.FloatField()
    largeur = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)

    class Meta:
        db_table = 'route_fusion'


class Holeintern(models.Model):
    id = models.IntegerField(primary_key=True)
    idhole = models.IntegerField()
    geom = models.PointField(srid=4326)
    description = models.CharField(max_length=50)

    class Meta:
        db_table = 'holeintern'


class Hospital(models.Model):
    gid = models.IntegerField(primary_key=True)
    osm_id = models.FloatField()
    osm_type = models.CharField(max_length=80)
    completene = models.DecimalField(max_digits=5, decimal_places=3)
    is_in_heal = models.CharField(max_length=80)
    amenity = models.CharField(max_length=80)
    speciality = models.CharField(max_length=80)
    addr_stree = models.CharField(max_length=80)
    operator = models.CharField(max_length=80)
    water_sour = models.CharField(max_length=80)
    changeset = models.IntegerField(db_column='changeset_')
    insurance = models.CharField(max_length=80)
    staff_doct = models.CharField(max_length=80)
    contact_nu = models.CharField(max_length=80)
    uuid = models.CharField(max_length=80)
    electricit = models.CharField(max_length=80)
    opening_ho = models.CharField(max_length=80)
    operationa = models.CharField(max_length=80)
    source = models.CharField(max_length=80)
    is_in_he_1 = models.CharField(max_length=80)
    hidden = models.SmallIntegerField()
    changese_1 = models.IntegerField()
    emergency = models.CharField(max_length=80)
    changese_2 = models.DateTimeField()
    addr_house = models.CharField(max_length=80)
    addr_postc = models.CharField(max_length=80)
    health_ame = models.CharField(max_length=80)
    addr_city = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    staff_nurs = models.CharField(max_length=80)
    changese_3 = models.CharField(max_length=80)
    wheelchair = models.CharField(max_length=80)
    beds = models.CharField(max_length=80)
    url = models.CharField(max_length=80)
    dispensing = models.CharField(max_length=80)
    healthcare = models.CharField(max_length=80)
    operator_t = models.CharField(max_length=80)
    geom = models.PointField(srid=4326, db_column='geom')

    class Meta:
        db_table = 'hospital'


# environment
class Environment(models.Model):
    gid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    idroadno = models.IntegerField()
    description = models.CharField(max_length=50)
    effectif = models.BigIntegerField()
    geom = models.PointField(srid=4326)

    class Meta:
        db_table = 'environment'



class Description(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'description'