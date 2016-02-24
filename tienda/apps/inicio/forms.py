# -*- encoding: utf-8 -*-

from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

from django import forms


class ContactForm(forms.Form):
    email  = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email','class':'form-control input-sm'}), required=True)
    titulo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Título','class':'form-control input-sm'}), required=True)
    texto  = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Texto','class':'form-control input-sm'}), required=True)

    def send_email(self):
        print "Enviando Email..."
        #======Primer Metodo======
        #subject = 'Correo de Contacto'
        #msj = u"Bienvenido a la aplicación, gracias por usar%s"%(texto)
        #from_email = settings.EMAIL_HOST_USER
        #to_list = [email,settings.EMAIL_HOST_USER]
        #send_mail(subject,msj, from_email, to_list, fail_silently=True)

        #======Primer Metodo======
        to_admin = [settings.EMAIL_HOST_USER]
        subject = 'Correo de Contacto'
        htmlContent = u"<p>Bienvenido a la aplicación, gracias por usarla<p> <br><br> %s"%(self.texto)
        msj = EmailMultiAlternatives(subject, htmlContent, 'from@server.com', to_admin)
        msj.attach_alternative(htmlContent, 'text/html')
        msj.send()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

