from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Arendator, Contract
from .forms import PostForm, ArendatorForm, ContractForm
from django.utils import timezone


# Create your views here.
#---------------------------------------------------------------------------------------
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'rpapp/post_list.html', {'posts': posts})

def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'rpapp/contract_list.html', {'contracts': contracts})

def post_free_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'rpapp/free.html', {'posts': posts})

def post_leased_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'rpapp/leased.html', {'posts': posts})

def arendator_list(request):
    arendators = Arendator.objects.all()
    return render(request, 'rpapp/arendator_list.html', {'arendators': arendators})
#---------------------------------------------------------------------------------------
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.picture = request.POST["picture"]
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'rpapp/post_edit.html', {'form': form})

def contract_new(request):
    if request.method == "POST":
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.author = request.user
            contract.contract_file = request.POST["contract_file"]
            contract.save()
            return redirect('contract_detail', pk=contract.pk)
    else:
        form = ContractForm()
    return render(request, 'rpapp/contract_edit.html', {'form': form})

def arendator_new(request):
    if request.method == "POST":
        form = ArendatorForm(request.POST, request.FILES)
        if form.is_valid():
            arendator = form.save(commit=False)
            arendator.author = request.user
            arendator.photo = request.POST["photo"]
            arendator.save()
            return redirect('arendator_detail', pk=arendator.pk)
    else:
        form = ArendatorForm()
    return render(request, 'rpapp/arendator_edit.html', {'form': form})
#---------------------------------------------------------------------------------------
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'rpapp/post_edit.html', {'form': form})

def contract_edit(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.author = request.user
            contract.save()
            return redirect('contract_detail', pk=contract.pk)
    else:
        form = ContractForm(instance=contract)
    return render(request, 'rpapp/contract_edit.html', {'form': form})

def arendator_edit(request, pk):
    arendator = get_object_or_404(Arendator, pk=pk)
    if request.method == "POST":
        form = ArendatorForm(request.POST, instance=arendator)
        if form.is_valid():
            arendator = form.save(commit=False)
            arendator.author = request.user
            arendator.save()
            return redirect('arendator_detail', pk=arendator.pk)
    else:
        form = ArendatorForm(instance=arendator)
    return render(request, 'rpapp/arendator_edit.html', {'form': form})
#---------------------------------------------------------------------------------------
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'rpapp/post_draft_list.html', {'posts': posts})

#---------------------------------------------------------------------------------------
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'rpapp/post_detail.html', {'post': post})

def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'rpapp/contract_detail.html', {'contract': contract})

def arendator_detail(request, pk):
    arendator = get_object_or_404(Arendator, pk=pk)
    return render(request, 'rpapp/arendator_detail.html', {'arendator': arendator})
#---------------------------------------------------------------------------------------
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def contract_remove(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    contract.delete()
    return redirect('contract_list')

def arendator_remove(request, pk):
    arendator = get_object_or_404(Arendator, pk=pk)
    arendator.delete()
    return redirect('arendator_list')
#---------------------------------------------------------------------------------------
