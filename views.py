from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RentalApplication, RentalAgreement, Payment
from .forms import RentalApplicationForm, RentalAgreementForm, PaymentForm
from properties_app.models import Property

@login_required
def rental_application_create(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        form = RentalApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.tenant = request.user
            application.property = property
            application.save()
            return redirect('property_detail', pk=property_id)
    else:
        form = RentalApplicationForm()
    return render(request, 'rentals/rental_application_form.html', {'form': form, 'property': property})

@login_required
def rental_application_list(request):
    if request.user.user_type == 'owner':
        applications = RentalApplication.objects.filter(property__owner=request.user)
    elif request.user.user_type == 'tenant':
        applications = RentalApplication.objects.filter(tenant=request.user)
    else:
        applications = RentalApplication.objects.all()
    return render(request, 'rentals/rental_application_list.html', {'applications': applications})

@login_required
def rental_application_update(request, pk):
    application = get_object_or_404(RentalApplication, pk=pk)
    if request.method == 'POST':
        form = RentalApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('rental_application_list')
    else:
        form = RentalApplicationForm(instance=application)
    return render(request, 'rentals/rental_application_form.html', {'form': form, 'application': application})

@login_required
def rental_agreement_create(request, application_id):
    application = get_object_or_404(RentalApplication, pk=application_id)
    if request.method == 'POST':
        form = RentalAgreementForm(request.POST)
        if form.is_valid():
            agreement = form.save(commit=False)
            agreement.tenant = application.tenant
            agreement.property = application.property
            agreement.save()
            application.status = 'approved'
            application.save()
            return redirect('rental_agreement_detail', pk=agreement.pk)
    else:
        form = RentalAgreementForm()
    return render(request, 'rentals/rental_agreement_form.html', {'form': form, 'application': application})

@login_required
def rental_agreement_detail(request, pk):
    agreement = get_object_or_404(RentalAgreement, pk=pk)
    return render(request, 'rentals/rental_agreement_detail.html', {'agreement': agreement})

@login_required
def payment_create(request, agreement_id):
    agreement = get_object_or_404(RentalAgreement, pk=agreement_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.rental_agreement = agreement
            payment.save()
            return redirect('rental_agreement_detail', pk=agreement_id)
    else:
        form = PaymentForm()
    return render(request, 'rentals/payment_form.html', {'form': form, 'agreement': agreement})

@login_required
def payment_history(request, agreement_id):
    agreement = get_object_or_404(RentalAgreement, pk=agreement_id)
    payments = Payment.objects.filter(rental_agreement=agreement)
    return render(request, 'rentals/payment_history.html', {'payments': payments, 'agreement': agreement})