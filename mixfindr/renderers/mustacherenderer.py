import os
from pyramid.asset import resolve_asset_spec
from pyramid.path import package_path
import pystache


# moustache templates
class MustacheRendererFactory(object):
    def __init__(self, info):
        self.info = info

    def __call__(self, value, system):
        package, filename = resolve_asset_spec(self.info.name)
        template = os.path.join(package_path(self.info.package), filename)
        template_fh = open(template)
        template_stream = template_fh.read()
        template_fh.close()
        return pystache.render(template_stream, value)
