from setuptools import setup, find_packages

setup(
    name='cms-talentpool',
    version='0.1',
    description='CMS apps to collect and display people according skills',
    author='Alban Tiberghien',
    author_email='alban.tiberghien@gmail.com',
    url='http://github.com/atibergien/cms-talentpool',
    packages=find_packages(),
    install_requires=[
        'django-haystack',
        'django-autoslug',
        'pillow',
        'django-imagekit',
	'django-ckeditor',
    ],
    keywords='django cms skills talent pool',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
