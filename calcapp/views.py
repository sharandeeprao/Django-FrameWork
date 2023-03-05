from django.shortcuts import render
from calcapp.forms import Calcform


# Create your views here.

def calc(request):
    form = Calcform()
    # m=login.objects.all()
    if request.method == 'POST':
        form = Calcform(request.POST)
        if 'submit_button' in request.POST and form.is_valid():
            expression_value = form.cleaned_data['expression']
            result_value = process_input(expression_value) # Replace with your own function to process input
            form.fields['result'].widget.attrs['value'] = result_value
        elif 'reset_button' in request.POST:
            form = Calcform()
    else:
        form = Calcform()

    
    


    return render(request,'calc.html',{'form': form})


def process_input(exp):

    
    li = []
    char = []
    for i in range(len(exp)):

        if i%2!=0:
            char.append(exp[i])
        else:
            li.append(exp[i])
    x1=int(li[0])
    for i in range(len(li)-1):

        
        x2=int(li[i+1])
       
        res=0

        if char[i]=='+':
            res = x1+x2
            x1=res
        elif char[i]=='-':
            res = x1-x2
            x1=res
        elif char[i]=='*':
            res = x1*x2
            x1=res
        elif char[i]=='/':
            res = x1/x2
            x1=res

    
        


    return str(x1)



