class MapView:
    def get_theme(self):
        pass

class SatelliteMapView(MapView):
    def get_theme(self):
        return "Satellite theme"
    
class BlockMapView(MapView):
    def get_theme(self):
        return "Block theme"
    
class Map:
    def render(self):
        pass

class WorldMap(Map):
    def __init__(self, map_view: MapView) -> None:
        self.map_view = map_view
    
    def render(self):
        print(f"World map in {self.map_view.get_theme()}")
    
class ExplorerMap(Map):
    def __init__(self, map_view: MapView) -> None:
        self.map_view = map_view
    
    def render(self):
        print(f"Explorer map in {self.map_view.get_theme()}")
    
if __name__ == "__main__":
    WorldMap(BlockMapView()).render()
    ExplorerMap(SatelliteMapView()).render()