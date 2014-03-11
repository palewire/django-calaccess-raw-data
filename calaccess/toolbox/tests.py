#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase


class ToolboxTest(TestCase):
    
    def test_unicodecsv(self):
        """
        Test simple usage of the unicodecsv toy.
        """
        import csv
        from toolbox import unicodecsv
        import StringIO
        d = StringIO.StringIO()
        d.write("Name,Type,County")
        d.write("La Cañada Flintridge,Neighborhood,L.A.County")
        reader = unicodecsv.UnicodeDictReader(d)
        self.assertEqual(type(list(reader)), type([]))
