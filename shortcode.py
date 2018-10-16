# -*- coding: utf-8 -*-
import pathlib
import shutil

from nikola.plugin_categories import ShortcodePlugin
from nikola.utils import makedirs


class CopyShortcodePlugin(ShortcodePlugin):
    name = "copy_shortcode"

    def set_site(self, site):
        super(CopyShortcodePlugin, self).set_site(site)
        self.site.register_shortcode('copy', self.handler)

    def handler(self, src_path, dst_path='.', post=None, **option):
        src = pathlib.Path(post.source_path).parent
        dst = pathlib.Path('output') / post.folder / post.meta('slug') / dst_path
        
        for s in src.glob(src_path):
            d = dst / s.name
            if not d.parent.exists():
                makedirs(str(d.parent))
            shutil.copyfile(s, d)
        return '', []
