from django.shortcuts import render
from .models import Category  # Adjust the import based on your actual model

def menu_view(request):
    # Get all categories
    categories = Category.objects.all()
    
    # Fetch menu items for specific categories
    coffee_items = categories.get(name='Coffee').menuitem_set.all() if categories.filter(name='Coffee').exists() else []
    pastry_items = categories.get(name='Pastries').menuitem_set.all() if categories.filter(name='Pastries').exists() else []
    
    # Pass the categories and menu items to the template context
    context = {
        'categories': categories,
        'coffee_items': coffee_items,
        'pastry_items': pastry_items,
    }
    
    return render(request, 'menu.html', context)
