from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

requirements = []
try:
    with open("requirements.txt", "r", encoding="utf-8") as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass

setup(
    name="hello-pkg-manoel-jr",
    version="0.1.0",
    author="Manoel FN Jr",
    author_email="...",
    description="Pacote que exibe Hello, World",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mfnjr/hello-pkg-manoel-jr",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'hello-world=hello_pkg_manoel_jr.hello:say_hello',
        ],
    },
)
