"""
Krackn AI Assistant Setup
"""

import os
from setuptools import setup, find_packages

def read_version():
    """Read version from krackn/__init__.py"""
    with open(os.path.join("krackn", "__init__.py"), "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"')
    return "0.1.0"

def read_readme():
    """Read the README.md file"""
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Krackn AI Assistant - AI-powered development tool"

setup(
    name="krackn",
    version=read_version(),
    description="AI-powered development assistant with FreeLoder technology",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="Krackn Team",
    author_email="support@krackn.ai",
    url="https://github.com/krackn88/krackn",
    packages=find_packages(exclude=['tests*']),
    python_requires=">=3.8",
    install_requires=[
        "PyQt6>=6.4.0",
        "PyQt6-QScintilla>=2.13.3",
        "aiohttp>=3.8.0",
        "pyyaml>=6.0",
        "GitPython>=3.1.0",
        "cryptography>=3.4.0",
        "toml>=0.10.2",
        "rich>=12.0.0"
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.5',
            'twine>=3.4.2',
            'build>=0.7.0'
        ]
    },
    entry_points={
        "console_scripts": [
            "krackn=krackn.app:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Editors :: Integrated Development Environments (IDE)"
    ],
    keywords="ai development assistant code generation",
    project_urls={
        "Bug Tracker": "https://github.com/krackn88/krackn/issues",
        "Source Code": "https://github.com/krackn88/krackn",
        "Documentation": "https://github.com/krackn88/krackn/blob/main/README.md"
    },
    package_data={
        'krackn': ['config/*.yaml', 'resources/*'],
    },
    include_package_data=True,
    zip_safe=False
)
