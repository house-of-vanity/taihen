import setuptools

# reqs = (line.strip() for line in open("requirements.txt"))
LONG_DESC = open('README.md').read()
setuptools.setup(
    name="taihen",
    version="0.1",
    author="Time Traveller, Ultradesu",
    author_email="time.traveller.san@gmail.com, ultradesu@hexor.ru",
    description="Play music from private music library using HTTPS.",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url="https://github.com/house-of-vanity/taihen",
    packages=setuptools.find_packages(),
    license="GPLv3",
    install_requires=[
        'pafy>=0.5.4',
        'python-dateutil>=2.7.5',
        'python-mpv>=0.3.9',
        'urwid>=2.0.1',
        'virtualenv>=16.0.0',
        'youtube-dl>=2019.5.20',
    ],
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    entry_points={"console_scripts": ["taihen=taihen.__init__:main"]},
)
