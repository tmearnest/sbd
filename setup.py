from setuptools import setup, find_packages
from glob import glob

setup(name='sbd',
      version='0.0.3',
      packages=find_packages(),
      description='Simple bibliography manager',
      long_description=open("README.md").read().strip(),
      author='Tyler M. Earnest',
      author_email='tylere@rne.st',
      url='https://github.com/tmearnest/sbd',
      data_files=[('sbd/templates', glob("sbd/templates/*"))],
      license='MIT License',
      entry_points = {"console_scripts": ['sbd = sbd.EntryPoint:main']},
      install_requires = ["flask", "inotify", "jinja2", "pdfminer.six",
                          "prompt_toolkit", "pygments",
                          "python-dateutil", "requests", "termcolor",
                          "unidecode"])
