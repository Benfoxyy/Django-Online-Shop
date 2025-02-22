upstream backend {
    server backend:8000;  # Backend service name and port
}

server {
    listen 80;

    location /static/ {
        alias /home/app/static/;
    }

    location /media/ {
        proxy_pass http://minio:9000/media/;
    }

    location /favicon.ico {
        access_log off;  # Disable logging for favicon requests
        log_not_found off;  # Suppress "not found" logs
        return 204;
    }

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        error_log /var/log/nginx/error.log debug;  # Enable debug logging for this location
    }
}
