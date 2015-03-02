from tethys_apps.base import TethysAppBase, url_map_maker


class TethysToolsforHydroShare(TethysAppBase):
    """
    Tethys app class for Tethys Tools for HydroShare.
    """

    name = 'Tethys Tools for HydroShare'
    index = 'tethys_hstools:home'
    icon = 'tethys_hstools/images/icon.gif'
    package = 'tethys_hstools'
    root_url = 'tethys-hstools'
    color = '#2ecc71'
        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='tethys-hstools/res/{res_id}/fn/{filename}',
                           controller='tethys_hstools.controllers.restcall'),

                    UrlMap(name='home',
                           url='tethys-hstools/',
                           controller='tethys_hstools.controllers.home'),

                    UrlMap(name='postexample',
                           url='tethys-hstools/postexample',
                           controller='tethys_hstools.controllers.postexample'),



        )

        return url_maps