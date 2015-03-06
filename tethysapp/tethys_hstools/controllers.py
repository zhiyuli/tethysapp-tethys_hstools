from django.shortcuts import render

from utilities import *

#test comment
#Base_Url_HydroShare REST API
url_base='http://dev.hydroshare.org/hsapi/resource/{0}/files/{1}'

##Call in Rest style
#http://127.0.0.1:8000/apps/tethys-hstools/res/72b1d67d415b4d949293b1e46d02367d/fn/referencetimeseries-2_23_2015-wml_2_0.wml/
def restcall(request,res_id,filename):

    print "restcall",res_id,filename
    url_wml= url_base.format(res_id,filename)

    response = urllib2.urlopen(url_wml)

    html = response.read()

    timeseries_plot = chartPara(html,filename)

    context = {"timeseries_plot":timeseries_plot}

    return render(request, 'tethys_hstools/home.html', context)

#Normal Get or Post Request
#http://dev.hydroshare.org/hsapi/resource/72b1d67d415b4d949293b1e46d02367d/files/referencetimeseries-2_23_2015-wml_2_0.wml/
#http://127.0.0.1:8000/apps/tethys-hstools/?filename=referencetimeseries-2_23_2015-wml_2_0.wml&res_id=72b1d67d415b4d949293b1e46d02367d
def home(request):

    filename=None
    res_id=None
    url_wml=None

    if request.method == 'POST' and 'res_id' in request.POST and 'filename' in request.POST:
       #print request.POST
       filename = request.POST['filename']
       res_id=  request.POST['res_id']
       url_wml= url_base.format(res_id,filename)
    elif request.method == 'GET' and 'res_id' in request.GET and 'filename' in request.GET:
        print request.GET
        filename = request.GET['filename']
        res_id = request.GET['res_id']
        url_wml= url_base.format(res_id,filename)

    if url_wml is None:
        filename = 'KiWIS-WML2-Example.wml'
        url_wml='http://www.waterml2.org/KiWIS-WML2-Example.wml'

    print url_wml

    response = urllib2.urlopen(url_wml)

    html = response.read()

    timeseries_plot = chartPara(html,filename)

    context = {"timeseries_plot":timeseries_plot}
    return render(request, 'tethys_hstools/home.html', context)


def postexample(request):

    name = ''

    # Define Gizmo Options
    text_input_options_res_id = {'display_text': 'Res ID',
                          'name': 'res_id',
                            'initial': '72b1d67d415b4d949293b1e46d02367d'}

    text_input_options_filename = {'display_text': 'Filename',
                          'name': 'filename',
                          'initial': 'referencetimeseries-2_23_2015-wml_2_0.wml'}

    # Check form data

    # Create template context dictionary
    context = {'name': name,
               'text_input_options_res_id': text_input_options_res_id,
               'text_input_options_filename':text_input_options_filename
               }

    return render(request, 'tethys_hstools/postexample.html',context)
