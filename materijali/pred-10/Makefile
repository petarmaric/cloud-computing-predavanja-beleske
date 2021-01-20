DOCKER_IMAGE = petarmaric/cloud-computing-predavanja:2020-pred-10

run: build .env
	docker-compose up --build

build:
	docker build . --tag $(DOCKER_IMAGE)

.env: .env.example
	cp .env.example .env

publish: build
	docker image push $(DOCKER_IMAGE)

destroy:
	docker-compose down
	cdk destroy --force

deploy: publish
	cdk deploy --require-approval never
