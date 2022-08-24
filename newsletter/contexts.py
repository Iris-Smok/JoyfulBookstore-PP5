from .forms import SubscriberForm


def subscribe_form_global(request):
    subscribe_form = SubscriberForm()
    return {'subscribe_form': subscribe_form}
