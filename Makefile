.PHONY: build

clean:
	@rm -rf build
	@rm -rf dist
	@rm -rf src/i18n_iso_countries.egg-info
	@rm -rf i18n_iso_countries.egg-info

build:
	@make clean
	@python setup.py bdist_wheel