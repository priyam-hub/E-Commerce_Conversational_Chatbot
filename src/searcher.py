from config import CLUSTER_URL
from config import COLLECTION_NAME
from config import QDRANT_API_KEY
from qdrant_client import QdrantClient
import random

# Initialize the Qdrant client
client = QdrantClient(url     = CLUSTER_URL, 
                      api_key = QDRANT_API_KEY
)

def search_collection(colour="NA", individual_category="NA", category="NA", category_by_gender="NA"):

    filters = []
    
    if colour != "NA":
        filters.append(lambda point: point.payload.get("colour") == colour)
    
    if individual_category != "NA":
        filters.append(lambda point: point.payload.get("Individual_category") == individual_category)
    
    if category != "NA":
        filters.append(lambda point: point.payload.get("Category") == category)
    
    if category_by_gender != "NA":
        filters.append(lambda point: point.payload.get("category_by_Gender") == category_by_gender)

    # Retrieve and filter points
    all_points = []
    next_page  = None

    while True:
        response, next_page = client.scroll(collection_name = COLLECTION_NAME, 
                                            limit           = 1000, 
                                            offset          = next_page
        )

        all_points.extend(response)

        if not next_page:
            break

    # Apply filters if any
    if filters:
        filtered_points = [
            point for point in all_points
            if all(f(point) for f in filters)
        ]
    else:
        filtered_points = random.sample(all_points, min(10, len(all_points)))

    # Output the results
    if filtered_points:
        results = [point.payload for point in filtered_points]
    else:
        random_points = random.sample(all_points, min(10, len(all_points)))
        results = [point.payload for point in random_points]

    return results
