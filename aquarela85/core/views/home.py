from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from aquarela85.core.helpers import utils


@login_required
def pagina_inicial(request):
    context = utils.get_context(request)
    return render(request, '{0}/index.html'.format(utils.path_template_home), context)
