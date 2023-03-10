from django.contrib import admin
from .models import Holedescription
from .models import Holelevel
from .models import Nationalroute
from .models import Workmanship

# Register your models here.
admin.site.register(Holedescription)
admin.site.register(Holelevel)
admin.site.register(Nationalroute)
admin.site.register(Workmanship)