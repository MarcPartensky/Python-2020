from github import Github
import os

g = Github(os.environ['PYGITHUB_TOKEN'])

# for repo in g.get_user().get_repos():
repo = g.get_user().get_repos()[0]
print(getattr(repo,'url'))
