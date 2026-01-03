from setuptools import setup, find_packages

setup(
    name="kirara-auto-qa-plugin",
    version="1.0.0",
    description="Auto QA Plugin for Kirara AI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'pywin32>=306',
        'pyautogui>=0.9.54',
    ],
    entry_points={
        'kirara_ai.plugins': [
            'auto_qa_plugin = auto_qa_plugin:AutoQAPlugin',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
