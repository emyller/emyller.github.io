# Generate pelican output and publish to Github
publish:
	pelican content
	ghp-import -b master -m 'Update output code' output
	git push --force $$(git remote) master
