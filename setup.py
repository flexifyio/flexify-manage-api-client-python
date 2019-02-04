# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.7.0-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "flexify-api"
VERSION = "2.7.0-SNAPSHOT"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Flexify.IO User REST API",
    author_email="info@flexify.io",
    url="https://github.com/flexifyio/flexify-manage-api-client-python",
    keywords=["Swagger", "Flexify.IO User REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    + Generate access token via &#x60;/rest/auth&#x60; + Authorize in Swagger UI using &#x60;Bearer TOKEN&#x60; + Enjoy Flexify.IO REST API  # noqa: E501
    """
)
