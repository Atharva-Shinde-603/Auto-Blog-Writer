from backend.wordpress_poster import post_to_wordpress

# Replace with your actual WordPress details
site_url = "http://atharvashinde603.wordpress.com"
username = "Atharva Shinde"
app_password = "AtharvaaShinde2025"
title = "My First Auto Blog Post"
content = "This blog was posted using Python + WordPress REST API."

# Test it
post_to_wordpress(site_url, username, app_password, title, content)
