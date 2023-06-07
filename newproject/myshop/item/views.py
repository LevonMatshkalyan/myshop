from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category,Item
from .forms import NewItemForm , EditItemForm
from django.db.models import Q



def detail(request , pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item_detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'add.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def delete(request , pk):
    item = get_object_or_404(Item,pk=pk , created_by = request.user)
    item.delete()
    return redirect('dashboard')

@login_required
def edit(request,pk):
    item = get_object_or_404(Item,pk=pk , created_by = request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item_detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'edit.html', {
        'form': form,
        'title': 'Edit item',
    })

def items(request):
    query = request.GET.get('query' , '')
    items = Item.objects.filter(is_sold = False)
    categories = Category.objects.all()
    category_anun = request.GET.get('category',0)

    if category_anun:
        items = Item.objects.filter(category_id = category_anun)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query) )

    return render(request , 'items.html' , 
                  {
                      'items':items,
                      'query':query,
                      'categories':categories,
                      'category_anun1':int(category_anun),
                  })