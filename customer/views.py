from django.shortcuts import render, redirect
from .forms import CustomerRecords
from django.contrib.auth.decorators import login_required
from .models import customers
from django.contrib import messages

@login_required(login_url='home.login')
def allcustomers(request):
    all_customers = customers.objects.all()
    print('all customers')
    print(len(all_customers))
    return render(request, 'list_customer.html', {'all_customers':all_customers})

@login_required(login_url='home.login')
def AddCustomer(request):
    form = CustomerRecords(request.POST or None)
    if form.is_valid():
        old_customer_obj = form.save(commit=False)
        old_customer_obj.last_updated_by = request.user
        old_customer_obj.save()
        messages.success(request, 'Customer '+old_customer_obj.customer_name+' created successfully!!')
        return redirect('customer.list')
    return render(request, 'add_customer.html', {'form': form, 'todo': 'add'})

@login_required(login_url='home.login')
def DeleteCustomer(request, pk):
    selected_customer = customers.objects.get(id=pk)
    selected_customer.delete()
    messages.success(request, 'Customer '+selected_customer.customer_name+' deleted successfully!!')
    return redirect('customer.list')

@login_required(login_url='home.login')
def UpdateCustomer(request, pk):
    selected_customer = customers.objects.get(id=pk)
    form = CustomerRecords(request.POST or None, instance=selected_customer)
    if form.is_valid():
        old_customer_obj = form.save(commit=False)
        old_customer_obj.last_updated_by = request.user
        old_customer_obj.save()
        messages.success(request, 'Customer '+ selected_customer.customer_name +' updated sucessfully!!')
        return redirect('customer.list')
    return render(request, 'add_customer.html', {'form':form, 'todo': 'edit'})
