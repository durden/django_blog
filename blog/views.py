from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import list_detail, date_based
from models import Post, Category

def blog_generic_view(request, redirect_to, **view_args):
    """
    Generic view to append default args before passing to primary view

    request     - Request
    redirect_to - View function to process final request
    view_args   - Dictionary of args to pass to final view
    """

    # Allow caller to pass queryset or use all post objects
    view_args['queryset'] = view_args.get('queryset', Post.objects.all())
    view_args['template_object_name'] = 'post'

    return redirect_to(request, **view_args)

def blog_posts_by_category(request, category_id):
    """
    Handle listing all blog posts by category

    request     - Request
    category_id - ID of category to display posts for
    """

    category = get_object_or_404(Category, pk=category_id)
    return blog_generic_view(request, list_detail.object_list,
                            queryset=category.post_set.all())

def blog_post_search(request):
    if 's' in request.GET and request.GET['s']:
        s = request.GET['s']
        return blog_generic_view(request, list_detail.object_list,
                                    queryset=Post.objects.search(s),)
    else:
        return render_to_response('blog/invalid_search.html')
