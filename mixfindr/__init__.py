from pyramid.config import Configurator
import os
import redis
from retools import global_connection
from urlparse import urlparse


# working directory
here = os.path.dirname(os.path.abspath(__file__))

# configure redis
redis_url = urlparse(os.getenv('REDISTOGO_URL', 'redis://localhost:6379'))

redis_host = '%s%s' % (redis_url.hostname, redis_url.path)
redis_port = redis_url.port
global_connection.redis = redis.Redis(host=redis_host, port=redis_port)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # add moustache renderer
    config.add_renderer(name='.mustache',
                        factory='mixfindr.renderers.mustacherenderer.MustacheRendererFactory')

    # routes setup
    config.add_route('index', '/')
    config.add_route('artist', '/artist/{id}')
    config.add_route('api_artist', '/api/artist/{id}')
    config.add_route('user', '/user/{id}')

    # scan for @view_config and @subscriber decorators
    config.scan()
    return config.make_wsgi_app()
