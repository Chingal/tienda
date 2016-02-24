from django.shortcuts import render, render_to_response, RequestContext
from django.views.generic import TemplateView, ListView, FormView

#================= Vista del Producto =================
from tienda.apps.ventas.models import Producto
from forms import ContactForm

class ProductView(ListView):
    template_name       = 'inicio/product.html'
    context_object_name = 'productos'
    queryset            = Producto.objects.filter(status=True)

class ContactView(FormView):
    template_name = 'inicio/contact.html'
    form_class    = ContactForm

    print template_name

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super(ContactView, self).form_valid(form)