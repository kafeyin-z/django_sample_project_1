from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from blog.models import blogModel
from blog.forms import blogForms


# Create your views here.

def ekle(request):
    form = blogForms()
    if request.method == 'POST':
        form = blogForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse('blog-detay', kwargs={'slug': post.slug}))
    context = {'form': form}
    return render(request, 'blog/ekle.html', context=context)


def guncelle(request, slug):
    data = get_object_or_404(blogModel, slug=slug)
    form = blogForms(instance=data)
    if request.method == "POST":
        form = blogForms(instance=data, data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse('blog-detay', kwargs={'slug': post.slug}))
    context = {'form': form, 'data': data}
    return render(request, 'blog/guncelle.html', context=context)


def sil(request, slug):
    post = get_object_or_404(blogModel, slug=slug)
    post.delete()
    return HttpResponseRedirect(reverse('blog-listele'))


def listele(request):
    model = blogModel.objects.all()
    context = {'posts': model}
    return render(request, 'blog/listele.html', context=context)


def detay(request, slug):
    post = get_object_or_404(blogModel, slug=slug)
    context = {'post': post}
    return render(request, 'blog/detay.html', context=context)
