from models import Post

def blog_generic_view(request, redirect_to, **view_args):
    view_args['queryset'] = Post.objects.all()
    view_args['template_object_name'] = 'post'

    return redirect_to(request, **view_args)
