from category.models import Category


def categories_links(request):
    links = Category.objects.filter(is_active=True)
    return {"links": links}
