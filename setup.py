from setuptools import setup, find_packages

setup(
    name="cmsplugin-bootstrap-carousel",
    packages=find_packages(),
    version="0.2.3",
    description="Bootstrap carousel plugin for django-cms",
    long_description=open('README.rst').read(),
    author="Nimbis Services, Inc.",
    author_email="devops@nimbisservices.com",
    url='https://github.com/nimbis/cmsplugin-bootstrap-carousel/',
    license="BSD",
    keywords=["django", "django-cms", "bootstrap", "carousel"],
    classifiers=[
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django"
        ],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "Django<1.10",
        "django-cms>2.4",
        "Pillow"
    ],
)
