from django.shortcuts import render,redirect
from Cars.models import Cars
from .forms import BookingForm
from django.contrib import messages
from .models import Booking
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponseBadRequest,HttpResponse
from django.contrib.auth.decorators import login_required


razorpay_client = razorpay.Client(
  auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

@login_required(login_url="SignIn")
def CarView(request,pk):
    car = Cars.objects.filter(id = pk)
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            sdate = form.cleaned_data.get("StartDate")
            edate = form.cleaned_data.get("EndDate")
            data = edate - sdate
            print(data.days)
            car = Cars.objects.get(id = pk)
            
            book = Booking.objects.filter(Car = car)
            flag = None
            for i in book:
                if sdate == i.StartDate:
                    flag = 1
                    break
                elif edate == i.EndDate:
                    flag = 1
                    break
                elif sdate >= i.StartDate and sdate <= i.EndDate:
                    flag = 1
                    break
                elif edate <= i.EndDate and edate >= i.StartDate:
                    flag = 1
                    break
            
            if flag is not None:
                messages.info(request,"Already Have booking On this date")
                return redirect('CarView',pk = pk)
                
            else:
                val = form.save()
                car = Cars.objects.get(id = pk)
                price = int(car.Rent)
                totalrent = int((int(data.days)+1) * price)
            
                val.Car = car
                val.amount = totalrent
                val.numberofdays = int(data.days)+1
                val.Customer = request.user
                val.save()
                vaiid = val.id
                messages.info(request,"Car Booked")
                return redirect('MakePayment',pk = vaiid)
    context = {
        "car":car,
        "form":form
    }
    return render(request,"carview.html",context)

@login_required(login_url="SignIn")
def MakePayment(request,pk):
    book = Booking.objects.get(id = pk)
    currency = 'INR'
    amount = int(book.amount) * 100 # Rs. 200
    

  # Create a Razorpay Order Pyament Integration.....
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                          currency=currency,
                          payment_capture='0'))

  # order id of newly created order.
    razorpay_order_id = razorpay_order["id"]
    callback_url = 'paymenthandler/'

  # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url 
    context['slotid'] = pk
    context["days"] = int(book.numberofdays)+1
    context["amount"] = book.amount
    
    return render(request,"payment.html",context)


@login_required(login_url="SignIn")
def Mybookings(request):
    book = Booking.objects.filter(Customer = request.user)
    # book = Booking.objects.all()
    context = {
        "book":book
    }
    return render(request,"bookings.html",context)

@login_required(login_url="SignIn")
def DeleteBooking(request,pk):
    book = Booking.objects.get(id = pk)
    book.delete()
    messages.info(request,"Your Booking Deleted")
    return redirect('Mybookings')

@login_required(login_url="SignIn")
def DeleteBookingAdmin(request,pk):
    book = Booking.objects.get(id = pk)
    book.delete()
    messages.info(request,"Your Booking Deleted")
    return redirect('BookingManagerView')


@csrf_exempt
def paymenthandler(request):
    book = Booking.objects.filter().last()
    booking = Booking.objects.get(id = book.id)
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

      # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                amount = int(book.amount) * 100 # Rs. 200
                try:
                    print("working 1")
                    x = razorpay_client.payment.capture(payment_id, amount)
                    print(x)
                    booking.paymentstatus = True
                    booking.save()
                    return render(request,'successpage.html',{"days":int(book.numberofdays)+1,"amount":book.amount})
          # render success page on successful caputre of payment
                except:
                    print("working 2")
                    return redirect('StatusChange')
                    
                    
          # if there is an error while capturing payment.
            else:
                return render(request, 'paymentfail.html')
        # if signature verification fails.    
        except:
            return HttpResponseBadRequest()
        
      # if we don't find the required parameters in POST data
    else:
  # if other than POST request is made.
        return HttpResponseBadRequest()
    
@login_required(login_url="SignIn")
def BookingManagerView(request):
    book = Booking.objects.all()
    # book = Booking.objects.all()
    context = {
        "book":book
    }
    
    return render(request,"booking.html",context)