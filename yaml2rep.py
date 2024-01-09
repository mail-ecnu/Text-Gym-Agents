import ruamel.yaml

yaml = ruamel.yaml.YAML()
data = yaml.load(open('environment.yaml'))

requirements = []
for dep in data['dependencies']:
    if isinstance(dep, str):
        package, package_version = dep.split('=')
        requirements.append(package + '==' + package_version)
    elif isinstance(dep, dict):
        for preq in dep.get('pip', []):
            requirements.append(preq)

with open('requirements.txt', 'w') as fp:
    for requirement in requirements:
       print(requirement, file=fp)