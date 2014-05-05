from setuptools import setup, find_packages
import os

import livinglots_friendlyowners


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
]

setup(
    author="Eric Brelsford",
    author_email="eric@596acres.org",
    name='django-livinglots-friendlyowners',
    version=livinglots_friendlyowners.__version__,
    description=('A Django app to let "friendly" owners opt their land into a '
                 'Living Lots site.'),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/596acres/django-livinglots-friendlyowners/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.6.1',
        'django-braces>=1.4.0',
        'django-monitor==0.2.1a',
    ],
    packages=find_packages(),
    include_package_data=True,
)
