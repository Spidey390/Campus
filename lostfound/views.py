from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from .models import Item, Claim
from .forms import ItemForm, ClaimForm

def home(request):
    return render(request, 'lostfound/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    my_items = Item.objects.filter(reported_by=request.user).order_by('-reported_at')
    return render(request, 'lostfound/dashboard.html', {'items': my_items})

@login_required
def report_item(request, status):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.reported_by = request.user
            item.status = status
            item.save()
            messages.success(request, f'Your {status.lower()} item has been reported!')
            return redirect('dashboard')
    else:
        form = ItemForm()
    return render(request, 'lostfound/item_form.html', {'form': form, 'status': status})

def found_items_list(request):
    query = request.GET.get('q')
    
    # This is the single, correct version of the function
    items = Item.objects.filter(
        status='Found', 
        is_verified=True
    ).exclude(
        claims__status='Approved'
    ).order_by('-reported_at')

    if query:
        items = items.filter(Q(item_name__icontains=query) | Q(description__icontains=query))
        
    return render(request, 'lostfound/found_items_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'lostfound/item_detail.html', {'item': item})

@login_required
def find_matches(request, pk):
    lost_item = get_object_or_404(Item, pk=pk, reported_by=request.user, status='Lost')
    potential_matches = Item.objects.filter(
        status='Found',
        is_verified=True,
        category=lost_item.category
    ).exclude(pk=lost_item.pk)
    context = {'lost_item': lost_item, 'matches': potential_matches}
    return render(request, 'lostfound/matches.html', context)

@login_required
def submit_claim(request, pk):
    item = get_object_or_404(Item, pk=pk, status='Found')
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.item = item
            claim.claimant = request.user
            claim.save()
            messages.success(request, 'Your claim has been submitted and is pending review.')
            return redirect('dashboard')
    else:
        form = ClaimForm()
    return render(request, 'lostfound/claim_form.html', {'form': form, 'item': item})