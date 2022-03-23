from django.shortcuts import render, get_object_or_404
from . models import Events

# Create your views here.
def index(request):
    dernier_event = Events.objects.order_by('id')
    context = {'event_list': dernier_event}
    return render(request, 'event/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    return render(request, 'event/detail.html', {'event':event})