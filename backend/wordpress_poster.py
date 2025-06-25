import requests
from requests.auth import HTTPBasicAuth

def post_to_wordpress(site_url, username, app_password, title, content):
    """
    Publishes a blog post to a WordPress site using REST API and app password.
    
    Args:
        site_url (str): Base URL of the WordPress site (e.g., https://example.wordpress.com)
        username (str): WordPress username
        app_password (str): WordPress application password
        title (str): Title of the blog post
        content (str): HTML/text content of the blog post
    
    Returns:
        bool: True if post successful, False otherwise
    """
    url = f"{site_url}/wp-json/wp/v2/posts"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "title": title,
        "content": content,
        "status": "publish"  # Or "draft" if you want user approval
    }

    try:
        response = requests.post(
            url,
            auth=HTTPBasicAuth(username, app_password),
            json=data,
            headers=headers
        )

        if response.status_code == 201:
            print("✅ Blog posted successfully!")
            return True
        else:
            print(f"❌ Failed to post. Status: {response.status_code}")
            print(response.text)
            return False
    except Exception as e:
        print("❌ Error posting to WordPress:", str(e))
        return False
