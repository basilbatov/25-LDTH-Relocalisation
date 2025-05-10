from src.utility.bounding_box import BoundingBox, Projection
from src.utility.get_satellite_image import get_satellite_image

def main():
    get_satellite_image(bbox=BoundingBox(
        min_lat=3220365.8666247735,
        max_lat=3226152.5903976946,
        min_lon=3594402.482942412,
        max_lon=3602683.382027172,
        projection=Projection.EPSG_3035
    ))

if __name__ == "__main__":
    main()