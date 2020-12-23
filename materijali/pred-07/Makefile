DOCKER_IMAGE = petarmaric/cloud-computing-predavanja:2020-pred-07
PORT = 8000

run: build
	docker run --rm -it -p $(PORT):$(PORT) $(DOCKER_IMAGE)

build:
	docker build . --tag $(DOCKER_IMAGE)

publish: build
	docker image push $(DOCKER_IMAGE)
