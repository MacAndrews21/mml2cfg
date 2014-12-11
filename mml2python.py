import simplejson as json

local_url = 'Projekte/mml2cfg/'
server_url = 'Projekte/mml2cfg/'

url = local_url
#url = server_url



inputFile = open(url + 'mml/project.mml')
#inputFile = open('sftp://komoot@komoot.koding.io/home/komoot/vector/tilestache__.cfg')
inputJson = json.load(inputFile) 
inputFile.close()

mml = json.JSONEncoder().encode(inputJson)
mmlDump = json.dumps(inputJson, indent=4)

print mmlDump

outputFile = open(url + 'project.py', 'w')
outputFile.write('project = ' + mmlDump)
outputFile.close()

