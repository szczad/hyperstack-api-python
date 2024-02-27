.PHONY: all generate clean

UID := $(shell id -u)
API_URL := https://infrahub-api-doc.nexgencloud.com/api.json
PKG_NAME := hyperstack
PKG_VERSION := 1.0.0

all: generate

generate: api.json
	docker container run \
		--rm \
		--user $(UID) \
		--tty \
		--interactive \
		--volume "$(PWD):/local" \
		openapitools/openapi-generator-cli \
		generate \
		--generator-name python \
		--input-spec "/local/api.json" \
		--output /local/ \
		--additional-properties packageName="$(PKG_NAME)" \
		--additional-properties packageVersion="$(PKG_VERSION)"

api.orig.json:
	curl "$(API_URL)" | jq . > api.orig.json

api.json: api.orig.json patch.jq
	jq -f 'patch.jq' api.orig.json > api.json

api.patch: api.orig.json api.json
	diff -u5 api.orig.json api.json > api.patch || true

clean:
	rm -f api.orig.json api.json api.patch
