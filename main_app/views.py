from django.shortcuts import render, redirect
from .models import Boardgame, Store
from .forms import ReviewForm

# Create your views here.
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BoardgameCreate(CreateView):
    model = Boardgame
    fields = '__all__'

class BoardgameUpdate(UpdateView):
    model = Boardgame
    fields = '__all__'

class BoardgameDelete(DeleteView):
    model = Boardgame
    success_url = '/boardgames/'

# Define the home view
def home(request):
    return HttpResponse('<h1>Welcome to the Board Game Collector</h1>')

def about(request):
    return render(request, 'about.html')

def boardgames_index(request):
    boardgames = Boardgame.objects.all()
    return render(request, 'bg/index.html', { 'boardgames': boardgames })

def boardgames_detail(request, boardgame_id):
    # boardgame_id refers to what was defined in urls.py ('boardgames/<int:boardgame_id>/')
    boardgame = Boardgame.objects.get(id=boardgame_id)
    # Get the stores the boardgame doesn't have already
    available_stores = Store.objects.exclude(id__in = boardgame.stores.all().values_list('id'))
    # instantiate ReviewForm to be rendered in the template
    review_form = ReviewForm()
    return render(request, 'bg/detail.html', {
        'boardgame': boardgame, 'review_form': review_form, 'stores': available_stores
        }) # :boardgame refers to the line above

def add_review(request, boardgame_id):
    # create a ModelForm instance using the data in request.POST
    form = ReviewForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save form to the db until it has the boardgame id assigned
        new_review = form.save(commit=False)
        new_review.boardgame_id = boardgame_id
        new_review.save()
    return redirect('detail', boardgame_id=boardgame_id)

def assoc_store(request, boardgame_id, store_id):
    boardgame = Boardgame.objects.get(id=boardgame_id)
    store = Store.objects.get(id=store_id)
    boardgame.stores.add(store_id)
    return redirect('detail', boardgame_id=boardgame_id)