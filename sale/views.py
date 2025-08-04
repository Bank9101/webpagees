from django.shortcuts import render

# Create your views here.

def index(req):
    
    return render(req, 'index.html')

def about(req):
    
    return render(req, 'about.html')

def contact(req):
    
    return render(req, 'contact.html')

def Mypage(req):
    
    return render(req, 'Mypage.html')

def for_view(req):
    context = {}
    multiplication_data = []
    
    if req.method == 'POST':
        try:
            number = int(req.POST.get('number', 0))
            if number > 0:
                # สร้างข้อมูลสูตรคูณ
                for i in range(1, 13):
                    multiplication_data.append({
                        'multiplier': i,
                        'result': number * i
                    })
                context['number'] = number
                context['multiplication_data'] = multiplication_data
            else:
                context['error'] = 'กรุณาใส่ตัวเลขที่มากกว่า 0'
        except ValueError:
            context['error'] = 'กรุณาใส่ตัวเลขที่ถูกต้อง'
    
    return render(req, 'for_view.html', context)