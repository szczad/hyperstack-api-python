.PHONY: all generate clean

UID := $(shell id -u)
API_URL := https://infrahub-api-doc.nexgencloud.com/api.json

all: generate

generate: openapi/api.json
	docker container run \
		--rm \
		--user $(UID) \
		--tty \
		--interactive \
		--volume "$(PWD):/local" \
		openapitools/openapi-generator-cli \
		generate \
		--config /local/openapi/config.yaml

openapi/api.orig.json:
	curl "$(API_URL)" | jq . > openapi/api.orig.json

openapi/api.json: openapi/api.orig.json openapi/patch.jq
	jq -f 'openapi/patch.jq' openapi/api.orig.json > openapi/api.json

openapi/api.patch: openapi/api.orig.json openapi/api.json
	diff -u5 openapi/api.orig.json openapi/api.json > openapi/api.patch || true

clean:
	rm -f openapi/api.orig.json openapi/api.json openapi/api.patch
