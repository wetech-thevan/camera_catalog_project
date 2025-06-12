# products/context_processors.py
def compare_context(request):
    return {
        'compare_list': request.session.get('compare_list', [])
    }