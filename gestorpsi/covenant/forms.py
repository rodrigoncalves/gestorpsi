# -*- coding: utf-8 -*-

"""
Copyright (C) 2008 GestorPsi

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""


from django import forms
from gestorpsi.covenant.models import Covenant


class CovenantForm(forms.ModelForm):

    class Meta:
        model = Covenant
        #fields = ('name', 'relation_level', 'responsible', 'active', 'comment')
