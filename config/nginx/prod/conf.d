upstream django_server {
    server django:8000;
}

server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://django_server;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_redirect off;
    }

    location /static/ {
        alias /code/static/;
    }

    location /media/ {
        alias /code/media/;
    }
}
