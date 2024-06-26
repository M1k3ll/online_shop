# from django.core.checks import messages
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from cart.forms import AddToCartProductForm
from products.models import Product, Comment
from .forms import CommentForm


# def test_messages(request):
#     result = "hello"
#     messages.success(request, 'this is the success messages')
#     messages.warning(request, 'this is success message')
#
#     return render(request,'products/testmessage.html')


class ProductListView(generic.ListView):  # class base view #CBV
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    # def get_success_url(self):
    #     return reverse('product_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        messages.success(self.request, 'Comment successfully created')

        return super().form_valid(form)

# class ProductDetailView(generic.DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#     context_object_name = 'products'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_form',] = CommentForm()
#         return context


# class CommentCreateView(generic.CreateView):
#     model = Comment
#     form_class = CommentForm

# def form_valid(self, form):
#     obj = form.save(commit=False)
#     obj.author = self.request.user
#     product_id = int(self.kwargs['product_id'])
#     product = get_object_or_404(Product, id=product_id)
#     obj.product = product
#     return super().form_valid(form)
