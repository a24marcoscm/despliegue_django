from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Publicacion
from login.models import User
import math



def homeSocial(request):
    if 'username' in request.session:
        return redirect(reverse('social:pageSocial', kwargs={'page_id': 0}))
    else:
        return redirect(reverse('login:login'))



def pageSocial(request, page_id):
    try:
        error_message = None
        if request.method == 'POST':

            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.FILES.get('image')
        
            if not title or not description:
                error_message = "El título y la descripción son obligatorios."
            else:

                publicacion = Publicacion(
                    title=title,
                    description=description,
                    author=User.objects.filter(username=request.session['username']).first()
                )
                if image:
                    publicacion.image = image
                publicacion.save()
                return redirect('social:pageSocial', page_id=0)

        publicaciones_pagina = 3
        max_pages = math.ceil(Publicacion.objects.count() / publicaciones_pagina)
        posts = Publicacion.objects.order_by('-created_at')[
            page_id * publicaciones_pagina:(page_id + 1) * publicaciones_pagina
        ]
        page_range = range(max_pages)

        return render(request, 'social/page_social.html', {
            'posts': posts,
            'page_id': page_id,
            'max_pages': max_pages,
            'page_range': page_range,
            'error_message': error_message,
        })
    except ValueError as e:
        return render(request, 'social/error.html', {'message': str(e)})
    

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('login:login')