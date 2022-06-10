FROM ubuntu:latest
WORKDIR /app
COPY . .
RUN apt-get install curl
CMD ["curl", "http://localhost:5000/generate-password/30/somethinghere/SOMETHINGHERE/30"]
EXPOSE 5000