from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from company_profile.forms import CompanyProfileForm
from company_profile.models import CompanyProfile


#TODO: add edit button to the company profile on the contract
#TODO: redirect to the company detail when clicking the sidebar button

"""
EDIT COMPANY PROFILE
"""
@login_required
def add_company_profile(request):
        user = request.user
        form = CompanyProfileForm(request.POST or None, request.FILES or None, user=user)
        exists = False

        if CompanyProfile.objects.filter(user=request.user).first() != None:
            company_profile = CompanyProfile.objects.filter(user=request.user).first().id
            exists = True

        if exists == False:
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect('detail_company_profile', company_profile)
            return render(request, 'add_company_profile.html', {'form': form})
        else:
            return redirect('detail_company_profile', company_profile)


"""
EDIT COMPANY PROFILE
"""
@login_required
def edit_company_profile(request, id):
    company_profile = get_object_or_404(CompanyProfile, pk=id)
    form = CompanyProfileForm(request.POST or None, request.FILES or None, instance=company_profile)

    if form.is_valid():
        form.save()
        return redirect('detail_company_profile', company_profile.id)
    return render(request, 'company_profile_form.html', {'form': form, 'company_profile': company_profile})



"""
DETAIL COMPANY PROFILE
"""
@login_required
def detail_company_profile(request, id):
    company_profile = get_object_or_404(CompanyProfile, pk=id)

    return render(request, 'detail_company_profile.html', {'company_profile': company_profile})