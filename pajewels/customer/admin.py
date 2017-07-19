# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from customer.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(UserAccount)
admin.site.register(UserRelation)