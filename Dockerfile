FROM nginx:alpine
LABEL version="1.0"
ENV AUTHOR="Your name"
WORKDIR  /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
