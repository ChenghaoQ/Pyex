import os

REPO_NAME = "what-is-this"
DEBUG = True


#Assumes the app is located in the same directory
#where this file reside
APP_DIR = os.path.dirname(os.path.abspath(__file__))  #the file ->'__file__' will be located ??????????????

def parent_dir(path):
	'''Return the parent of a directory.'''
	return os.path.abspath(os.path.join(path,os.pardir)) #???????????????

PROJECT_ROOT = parent_dir(APP_DIR)+'/posts'#Tell Frozen-Flask to build the static content to the project root instead of the default build/ directory. 
#为了部署在Github pages 上面，你需要将静态文件部署在项目根目录
FREEZER_DESTINATION =PROJECT_ROOT
#Since this is a repo page(not a Github user page).we neet to set the BASE_URL to the correct url as per GH pages' standards没理解这句
FREEZER_BASE_URL ="http://localhost/{0}".format(REPO_NAME)#We also need to explicitly set FREEZER_BASE_URL since Github Pages hosts your repo pages on http://username.github.io/your-reponame. 
FREEZER_REMOVE_EXTRA_FILES = False #如果该选项是TRUE，FREEZE执行后会删掉所有项目文件

FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR,'pages')
FLATPAGES_EXTENSION = '.md'#让FlatPages 去project/pages 查找.md 文件


