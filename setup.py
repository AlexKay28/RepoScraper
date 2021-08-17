from setuptools import setup, find_packages

install_requires = []

setup(
    name="RepoScraper",
    packages=find_packages(),
    package_data={"reposcraper": ["internal_data/*"]},
    description="repository info craper",
    version="0.0.1",
    url="https://github.com/AlexKay28/RepoScraper",
    author="Kaigorodov Alexander",
    author_email="kaygorodo2305@gmail.com",
    download_url="https://pypi.org/project/zarnitsa/",
    install_requires=install_requires,
    keywords=["scripts", "struct"],
    include_package_data=True,
)
