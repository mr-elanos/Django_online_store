from django.shortcuts import render
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart
from pages.utils import menu
from django.core.mail import send_mail
from magtrailer.KEY import from_email, recipient_list


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            send_mail('Нове замовлення в магазині MAG Trailer',
                      f'Зареєстровано нове замовлення:\n\n\n {order}',
                      from_email=from_email,
                      recipient_list=[recipient_list],
                      fail_silently=False,
                      )
            cart.clear()
            return render(request, 'orders/order/ok_order.html',
                          {'order': order, 'menu': menu, 'title': 'Замовлення прийнято'})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form, 'menu': menu, 'title': 'Підтвердження замовлення'})


def ok_order(request):
    return render(request, 'pages/ok_form.html', {'menu': menu, 'title': 'Звернення прийнято'})