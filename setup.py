from setuptools import find_packages, setup

setup(
    long_description_content_type='text/markdown',
    long_description="""# Markdown supported!\n\n* Cheer\n* Celebrate\n""",
    name='preln',
    packages=find_packages(include=['Preln']),
    version='0.1.0',
    description='A preprocessing libray for text in spanish',
    author='Adrián H.S & Raúl M.R',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)