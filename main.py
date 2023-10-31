import requests
import os

# Kong base URL (replace with my Kong configuration)
KONG_BASE_URL = "http://localhost:8001"

# Define the route path (demo route)
ROUTE_PATH = "/my-route"

# Define the asset storage directory (for simulation)
ASSET_STORAGE_DIR = "assets/"

# Create the asset storage directory if it doesn't exist
if not os.path.exists(ASSET_STORAGE_DIR):
    os.makedirs(ASSET_STORAGE_DIR)

def upload_asset(file_path):
    try:
        # Simulate asset upload by copying the file to the asset storage directory
        file_name = os.path.basename(file_path)
        asset_path = os.path.join(ASSET_STORAGE_DIR, file_name)
        with open(file_path, 'rb') as src_file, open(asset_path, 'wb') as dest_file:
            dest_file.write(src_file.read())

        # Generate a mock CDN URL for the uploaded asset
        cdn_url = f"{KONG_BASE_URL}{ROUTE_PATH}/assets/{file_name}"
        return cdn_url
    except Exception as e:
        print(f"Asset upload failed: {str(e)}")
        return None

def retrieve_asset(asset_filename):
    try:
        # Simulate asset retrieval by returning a mock CDN URL
        cdn_url = f"{KONG_BASE_URL}{ROUTE_PATH}/assets/{asset_filename}"
        return cdn_url
    except Exception as e:
        print(f"Asset retrieval failed: {str(e)}")
        return None

# Example:
mock_retrieve_url = retrieve_asset('asset.ext')
print(f"Retrieved Asset URL: {mock_retrieve_url}")
