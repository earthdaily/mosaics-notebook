import statistics
import math
import numpy as np
from osgeo import gdal
import rasterio
from rasterio.plot import show_hist, show
import matplotlib.pyplot as plt
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles, TileLayer, DrawControl, FullScreenControl, GeoJSON, Polygon


def plot_data(file_path, band_labels, show_bands, show_percentile=95):     
    """
    Simple function to plot data read from mosaic
    
    Args: 
        file_path: The imagery to plot
        band_labels: Descriptive labels corresponding to the X bands 
        show_bands: A list of 3 bands from band_data to display 
                    (e.g. [3, 2, 1] to display the 3rd, 2nd, and 1st band)
        show_percentile: Upper percentile trim for display scaling purposes 
    """
    
    ds = gdal.Open(file_path, gdal.GA_ReadOnly)
    band_data = np.array([ds.GetRasterBand(idx).ReadAsArray() for idx in show_bands])
    
    # Show unscaled DN values with histogram
    fig, (axrgb, axhist) = plt.subplots(1, 2, figsize=(20,10))
    show(band_data, ax=axrgb, title='Unscaled DN values')
    show_hist(band_data, bins=100, ax=axhist)
    plt.show()

    # Show with human friendly scaling
    img = band_data.transpose((1, 2, 0))
    plt.figure(figsize=(20, 20))
    img = img/np.percentile(img, show_percentile) # Very naive scaling. Change this if image is washed out or too dark
    plt.imshow(img)
    

class PreviewMap: 
    """
    Represents a preview map which the user can use to select an AOI for mosaic download
    """
    
    
    def __init__(self): 
        # Collect rectangle features from map
        self.mosaic_selection =  {
            'type': 'FeatureCollection',
            'features': []
        }


    def get_selected_utm_epsg(self): 
        """
        Get the closest UTM EPSG code for the selected AOI
        """

        geo_aoi = self.get_selected_lat_lon_corners()
        lon = statistics.mean([geo_aoi['ul_lng'], geo_aoi['lr_lng']])
        lat = statistics.mean([geo_aoi['ul_lat'], geo_aoi['lr_lat']])
        
        # Calculation from https://stackoverflow.com/a/40140326/4556479 
        utm_band = str((math.floor((lon + 180) / 6 ) % 60) + 1)
        if len(utm_band) == 1:
            utm_band = '0'+utm_band
        if lat >= 0:
            epsg_code = '326' + utm_band
            return f'EPSG:{epsg_code}'
        epsg_code = '327' + utm_band        
        return f'EPSG:{epsg_code}'

        
    def get_selected_lat_lon_corners(self):
        """
        Convert Rectangle feature selection to ul/lr lat/lng corners
        
        Returns: 
            dict of corners in {'ul_lat': ul_lat, 'ul_lng': ul_lng, 'lr_lat': lr_lat, 'lr_lng': lr_lng}
        """
        
        if not self.mosaic_selection['features']: 
            print('Please select an AOI first!')
            return 
        
        [ul_lng, lr_lat], _, [lr_lng, ul_lat], _, _ = self.mosaic_selection['features']['geometry']['coordinates'][0]

        return {
            'ul_lat': ul_lat,
            'ul_lng': ul_lng,
            'lr_lat': lr_lat,
            'lr_lng': lr_lng
        }
        
    
    def get_map(self, center, zoom, raster_for_footprint=None, polygon_for_footprint=None):
        """
        Shows interactive map for user to select AOI to for download
        
        Args: 
            center: Initial location to centre the map, as [latitude, longitude]
            zoom: Initial slippymaps zoom level to show the map at
            raster_for_footprint: Path to raster for which to show footprint
        """

        # Add map with rough footprint for mosaic
        preview_map = Map(basemap=basemaps.OpenStreetMap.Mapnik, center=center, zoom=zoom, scroll_wheel_zoom=True)
        
        if polygon_for_footprint is not None: 
            preview_map.add_layer(Polygon(
                locations=polygon_for_footprint,
                color="green",
                fill_color="green"
            ))

        # Disable every draw control but rectangle
        draw_control = DrawControl()
        draw_control.polyline =  {}
        draw_control.polygon = {}
        draw_control.circlemarker = {}
        draw_control.rectangle = {
            "shapeOptions": {
                "fillColor": "#fca45d",
                "color": "#fca45d",
                "fillOpacity": 0.2
            }
        }

        def handle_draw(draw_control_self, action, geo_json):
            # Take only the most recent recangle
            self.mosaic_selection['features'] = (geo_json)

        draw_control.on_draw(handle_draw)

        # Add rectangle controls
        preview_map.add_control(draw_control)

        # Enable full screen
        preview_map.add_control(FullScreenControl())

        # Display map
        return preview_map
