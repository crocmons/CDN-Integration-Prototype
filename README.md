# CDN-Integration-Prototype
# CDN Integration Prototype with Kong and Python

## Introduction

This README provides an overview of the CDN integration prototype using Kong and Python. The objective of this prototype is to demonstrate CDN functionality without implementing caching for a web application. This demonstration uses a simulated setup for educational and demonstration purposes.

## Prerequisites

- [Kong]([https://docs.konghq.com/gateway/latest/installation/]): Ensure that Kong is installed on your local machine or server.
- Python: Make sure you have Python installed, along with the `requests` library ( pip install requests).
- A web application URL (for simulation).

## Installation and Setup

1. **Kong Installation:**
   - Install Kong on your local machine following the installation guide for your platform here I'm using ubuntu linux system: [Kong Installation Guide](https://docs.konghq.com/gateway/latest/install/linux/ubuntu/).

2. **Kong Startup:**
   - Start the Kong API Gateway service:
     ```shell
     kong start
     ```

## Configuration in Kong

3. **Access Kong Admin API:**
   - Open your web browser and access Kong's Admin API interface, typically located at `http://localhost:8001`. This is where you'll configure Kong.

4. **Create a Dummy Service:**
   - Create a dummy service to represent your web application. Replace `http://example.com` with your actual web application URL:
     ```shell
     curl -i -X POST --url http://localhost:8001/services/ --data 'name=dummy-service' --data 'url=http://example.com'
     ```

5. **Create a Route for the Dummy Service:**
   - Create a route for the "dummy-service" to specify how incoming requests should be handled:
     ```shell
     curl -i -X POST --url http://localhost:8001/services/dummy-service/routes --data 'paths[]=/my-route'
     ```

## Simulate Asset Upload and Retrieval

6. **Python Functions:**
   - Implement Python functions for simulating asset upload and retrieval using the provided code. Replace placeholder URLs and paths with your actual configurations. The code includes the following functions:
     - `upload_asset(file_path)`: Simulate asset upload.
     - `retrieve_asset(asset_filename)`: Simulate asset retrieval.

7. **Test the Python Functions:**
   - Test the Python functions to ensure they work as expected. You can use the example provided in the code.



## Documentation

- The `assets/` directory is used for simulating asset storage. You can replace this with the actual asset storage mechanism in a real-world scenario.

- Additional documentation and configuration details can be added to further explain the setup and usage.

## Disclaimer

This prototype is for educational and demonstration purposes. In a production environment, actual CDN services and configurations would be used.

## Author

Ilma Salsabil


