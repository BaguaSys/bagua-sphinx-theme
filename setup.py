# Copyright 2020-2021 Faculty Science Limited
# Copyright 2021 Kuaishou AI Platform & DS3 Lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup
from pathlib import Path


README = Path(__file__).parent / "README.rst"


setup(
    name="bagua-sphinx-theme",
    description="A Sphinx theme for Bagua.",
    long_description=README.read_text(),
    author="Xiangru Lian",
    author_email="admin@mail.xrlian.com",
    license="Apache Software License",
    packages=["bagua_sphinx_theme"],
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    install_requires=["sphinx-rtd-theme==0.4.3"],
    package_data={
        "bagua_sphinx_theme": [
            "theme.conf",
            "*.html",
            "static/css/*.css",
            "static/images/*.svg",
            "static/images/*.ico",
        ]
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "sphinx.html_themes": ["bagua-sphinx-theme = bagua_sphinx_theme"],
    },
)
