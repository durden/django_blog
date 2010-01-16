from django.shortcuts import render_to_response

# Only useful if you want to add an extension to the template, otherwise
# just use direct_to_template -- from django.views.generic.simple
def static_page(response, template):
    template = '%s.html' % (template)
    return render_to_response(template)
