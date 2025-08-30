# Import the necessary libraries.
# If you don't have them, you can install them with:
# pip install Flask requests-tor flask-cors
from flask import Flask, request, Response
from flask_cors import CORS
from requests_tor import RequestsTor

# --- Configuration ---
# Define the host and port for our local web server.
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8006

# Create a Flask web application instance.
app = Flask(__name__)

# Enable CORS for all routes and all origins.
CORS(app)

# --- Server Route ---
# The root route ('/') is the main entry point for our server.
# It will handle all incoming requests.
@app.route('/')
def proxy_request():
    """
    Handles a request to the server, fetches content from a target URL
    through the Tor proxy, and returns the response.
    """
    # Get the 'url' query parameter from the incoming request.
    target_url = request.args.get('url')

    # Check if a URL was provided. If not, return an error message.
    if not target_url:
        return '<h1>Error: Please provide a URL in the query parameter.</h1><p>Example: http://127.0.0.1:8006/?url=http://example.com</p>', 400

    print(f"[*] Fetching URL through Tor proxy: {target_url}")

    try:
        # The correct way to use requests-tor is to create a RequestsTor object
        # and then use it to make your requests. This handles all the proxy
        # configuration correctly in the background.
        tor_requests = RequestsTor()
        
        # Make a GET request using the tor_requests object.
        # We use verify=False to avoid SSL errors common with proxies.
        # Timeout is set to avoid long waits if the connection fails.
        response = tor_requests.get(target_url, verify=False, timeout=10)

        # Create a new Flask Response object to return to the user's browser.
        flask_response = Response(response.content, status=response.status_code)
        
        return flask_response

    except Exception as e:
        # Catch any errors that occur during the request.
        error_message = f"Error connecting to target URL or proxy: {e}"
        print(f"[!] {error_message}")
        return f'<h1>Proxy Error</h1><p>{error_message}</p>', 500

# --- Main Entry Point ---
# The standard entry point for running a Flask application.
if __name__ == '__main__':
    # Run the server.
    app.run(host=SERVER_HOST, port=SERVER_PORT)