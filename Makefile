.PHONY: all generate clean remove

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

remove:
	rm -rf hyperstack docs test .github .openapi-generator .openapi-generator-ignore .gitlab-ci.yml .travis.yml README.md git_push.sh pyproject.toml requirements.txt setup.py setup.cfg test-requirements.txt tox.ini
