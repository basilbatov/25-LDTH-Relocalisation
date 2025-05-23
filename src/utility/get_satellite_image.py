import cv2
import numpy as np
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from src.utility.bounding_box import BoundingBox, Projection
    
def get_satellite_image(bbox: BoundingBox) -> np.ndarray:
    # High res 2021 satellite imagery from Copernicus
    # url = "https://image.discomap.eea.europa.eu/arcgis/rest/services/GioLand/VHR_2021_LAEA/ImageServer/exportImage"
    # High res 2018 satellite imagery from Copernicus
    url = "https://image.discomap.eea.europa.eu/arcgis/rest/services/GioLand/VHR_2018_LAEA/ImageServer/exportImage"

    # Bounding box is in EPSG:3035 (since it's LAEA projection)
    params = {
        "bbox": bbox.to_query_string(),
        "bboxSR": "3035",
        "size": "512,512",
        # "size": "1024,1024",
        # "size": "2048,2048",
        # "size": "5096,5096",
        # "size": "10192,10192", 
        "imageSR": "3035",
        "format": "png",  # can also be "tiff"
        "f": "image",
    }

    response = requests.get(url, params=params)

    try:
        response.raise_for_status()
        image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_UNCHANGED)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) # type: ignore
        plt.axis('off') # type: ignore
        plt.show() # type: ignore
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        print("Response content:", response.content)
    
    return image