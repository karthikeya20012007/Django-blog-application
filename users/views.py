from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created! You can Login now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        
        messages.success(request, f'Your Profile has Been Updated')
        return redirect('profile')
        #return render(request, 'users/profile.html') 
        # if we use render the website asks for 'confirm resubmission' every time we reload the page, hence we are using redirect
        # redirect uses get request, hence it loads without asking for resubmission.
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
            
    context = {
        'u_form':u_form,
        'p_form':p_form       
        }
    return render(request, 'users/profile.html',context) 