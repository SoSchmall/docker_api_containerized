# build docker images; if no errors then start containers
docker-compose build

if [ $? -eq 0 ]; then
    docker-compose up
else
    echo "docker-compose build failed"
fi