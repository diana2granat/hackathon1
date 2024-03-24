# frontend/views.py
from django.shortcuts import render
from .models import AddUser, Records  # Import your backend function

def index_view(request):
    if request.method == 'POST':
        # Process the form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')

        # Create an instance of AddUser model
        new_user = AddUser(first_name=first_name, last_name=last_name, email=email, phone=phone, city=city)
        # Save the instance to the database
        new_user.save()
        
        user = AddUser.objects.get(pk=1)  # Fetch the AddUser instance from the database
        records = Records(user)
        records.find_matching_opportunities()

        # Pass the results to the template rendering
        return render(request, 'frontend/index.html', {'matching_opportunities': matching_opportunities})
    else:
        return render(request, 'frontend/index.html')
