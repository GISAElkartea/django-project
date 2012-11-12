from setuptools import setup, find_packages
import sys, os

version = '0.1'

def description(filename):
    with open(filename) as description_file:
        description = description_file.read()
    return description

setup(name='django-project',
      version=version,
      description='Django project templates',
      long_description=description('README.md'),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Framework :: Buildout',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Build Tools',
          ],
      keywords=['django', 'fabric', 'buildout', 'paster'],
      author='Unai Zalakain (GISA Elkartea)',
      author_email='unai@gisa-elkartea.org',
      url='https://github.com/unaizalakain/django-project',
      license='GPLv3',
      zip_safe=False,
      packages=find_packages('django_project'),
      package_dir={'': 'django_project'},
      include_package_data=True,
      install_requires=[
          'setuptools',
          'PasteScript>=1.3',
          'Cheetah',
          'Fabric>=0.9.5',
          'inifaction',
      ],
      entry_points="""
      [paste.paster_create_template]
      django_project = django_project.pastertemplates:DjangoProjectTemplate
      """,
      )
