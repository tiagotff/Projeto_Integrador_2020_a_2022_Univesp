from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from cardapio_virtual.forms import ItemForm
from cardapio_virtual.models import Item
# Create your views here.
def emp(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ItemForm()
    return render(request,'index.html',{'form':form})
def show(request):
    itens = Item.objects.all()
    return render(request,"show.html",{'itens':itens})
def edit(request, id):
    item = Item.objects.get(id=id)
    return render(request,'edit.html', {'item':item})
def update(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST, instance = item)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'item': item})
def destroy(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect("/show")