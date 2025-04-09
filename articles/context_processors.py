from .models import Category

def categories_context(request):
    return {'categories': Category.objects.all()}
