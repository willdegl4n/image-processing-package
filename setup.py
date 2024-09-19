from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Processador_de_imagens",
    version="1.0.0",
    author="Willdeglan",
    #author_email="willdeglan@gmail.com",
    description="Image Processing Package using skimage",
    long_description=page_description,
    long_description_content_type="texto/Markdown",
    url="https://github.com/willdegl4n/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)

# Documentação:
# https://setuptools.readthedocs.io/en/latest/setuptools.html