import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="web",
    version="0.1.1",
    author="--",
    author_email="--",
    description="Web",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CS-UTEC/proyecto-web-elnombresiempreeslomasdificil",  # noqa
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        "Flask",
        "SQLAlchemy",
        "markdown",
        "pyxdg",
    ],
    entry_points={
        "console_scripts": [
            "web = web.web:main",
        ],
    },
    package_data={
        "": ["static/*/*", "templates/*/*"]
    },
    python_requires='>=3.3',
)
