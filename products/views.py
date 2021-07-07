from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from .models import Product, Category, ProductReview
from .forms import ProductForm, ProductReviewForm
from profiles.models import UserProfile


# Create your views here.


def all_products(request):
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please type product name to search")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    review_count=None
    on_profile_page =False
    rating_percentage = None
    indv_rating = None
    
    if request.method == 'POST':
       # once the form is posted collecting the user input
        review_form_data ={
        'review_headline':request.POST['review_headline'],
        'review_text':request.POST['review_text'],
        'rating':request.POST['rating'],          }       
        
        form = ProductReviewForm(review_form_data)
        if form.is_valid():
            data = form.save(commit=False) # review not saved yet            
            data.user = request.user                  
            data.product = product
            data.rating = form.cleaned_data['rating']
            data.save()             
            indv_rating = data.rating
            print(f'indviual{indv_rating}')
            data.product_id = Product.objects.get(id=product_id)
            messages.success(request, 'Your review is added')            
            on_profile_page=True
            return redirect(reverse('product_detail', args=[product.id]))
           
        else:            
            form = ProductReviewForm(instance=product)
            messages.error(request, 'Failed to add please check your form')            
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductReviewForm()  
        
    product_review = ProductReview.objects.filter(product_id=product_id)
    if product_review:
        on_profile_page=True        
        review_count = ProductReview.objects.filter(product_id=product_id).count()
        rating = form['rating']            
        rating_avarage = round(product_review.aggregate(Avg('rating'))['rating__avg'],2) 
        """ multiply the avarage with 100 and divide to 5 will give us the percentage
            I multiply by 20 which gives the same result."""
        rating_percentage = rating_avarage*20    
    else:
        rating_avarage = None
            
    
    template = 'products/product_detail.html'    
    context = {
        'product': product,
        'form':form,
        'product_review':product_review,
        'review_count': review_count,
        'rating_avarage':rating_avarage,
        'on_profile_page':on_profile_page,
        'rating_percentage':rating_percentage,
        'indv_rating':indv_rating,
        
    }
    return render(request,template , context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        template = 'products/add_product.html'
        context = {
            'form': form,
        }

    return render(request, template, context)
@login_required
def edit_product(request, product_id):
    """Edit a Product in the store """

    if not request.user.is_superuser:
       messages.error(request, 'Sorry, only store owners can do that.')
       return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, ' Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Deleting the product """

    if not request.user.is_superuser:
       messages.error(request, 'Sorry, only store owners can do that.')
       return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success('Product deleted!')
    
    return redirect(reverse('products'))

       


     

    

