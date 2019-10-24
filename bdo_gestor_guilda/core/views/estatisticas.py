from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from bdo_gestor_guilda.core.helpers import utils


@login_required
def index(request):
    context = utils.get_context(request)
    return render(request, '{0}/index.html'.format(utils.path_estatisticas), context)
