from django.shortcuts import render

import urllib2
from lxml import etree
from datetime import datetime
from datetime import timedelta
from utilities import *

def home(request):
    """
    Controller for the app home page.
    """
    response = urllib2.urlopen('http://www.waterml2.org/KiWIS-WML2-Example.wml')
    html = response.read()

    root = etree.XML(html)
    wml_version = get_version(root)

    ts={}
    if wml_version == '1':
        ts = parse_1_0_and_1_1(root)
    elif wml_version == '2.0':
        ts = parse_2_0(root)

    title_text="KiWIS-WML2-Example from "
    x_title_text = "Time"
    y_title_text = "Measures'"
    serise_text="KiWIS-WML2-Example"

    # Timeseries plot example
    timeseries_plot_object = {
        'chart': {
            'type': 'area',
            'zoomType': 'x'
        },
        'title': {
            'text': title_text
        },
        'xAxis': {
            'maxZoom': 3 * 24 * 3600000, # 30 days in milliseconds
            'type': 'datetime',
            'title': {
                'text': x_title_text
            }
        },
        'yAxis': {
            'title': {
                'text': y_title_text
            }
        },
        'legend': {
            'layout': 'vertical',
            'align': 'right',
            'verticalAlign': 'top',
            'x': -350,
            'y': 125,
            'floating': True,
            'borderWidth': 1,
            'backgroundColor': '#FFFFFF'
        },
        'series': [{
            'name': serise_text,
            'data':ts["for_highchart"]
        }]
    }


    timeseries_plot = {'highcharts_object': timeseries_plot_object,
                     'width': '500px',
                     'height': '500px'}


    context = {"timeseries_plot":timeseries_plot}

    return render(request, 'tethys_hstools/home.html', context)