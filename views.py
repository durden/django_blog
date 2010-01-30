from django.shortcuts import render_to_response

def static_page(response, template):
    """
    Wrapper to append .html to template and render it

    NOTE: Only useful if you want to add an extension to the template, otherwise
          just use direct_to_template -- from django.views.generic.simple
    """

    template = '%s.html' % (template)
    return render_to_response(template)
