from django.conf import settings

settings.configure(DEBUG=True)

from peliculas.models import Pelicula

for p in Pelicula.objects.all():
    print(p)
  