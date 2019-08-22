from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name="snmptrapseverity",
    version=version,
    description='Transmute SNMPTraps from remote mapping',
    url='https://github.com/dnhodgson/alerta-snmptrap-severity',
    license='Apache License 2.0',
    author='Darcy Hodgson',
    author_email='me@darcyhodgson.com',
    packages=find_packages(),
    py_modules=['snmptrapseverity'],
    install_requires=[],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'snmptrapseverity = snmptrapseverity:SNMPTrapSeverity'
        ]
    }
)
