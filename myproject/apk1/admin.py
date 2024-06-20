from django.contrib import admin
from .models import *

admin.site.site_header = "6ixty_wings Admin"
admin.site.site_title = "6ixty_wings Admin Portal"
admin.site.index_title = "Welcome 6ixty_wings Admin"
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)