from setuptools import setup, find_packages

# Read requirements.txt and use its contents for the install_requires option
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A simple math quiz game',
    author='xihao wu',
    author_email='xihao.wu@fau.de',
    install_requires=required,
    entry_points='''
        [console_scripts]
        math_quiz=math_quiz.math_quiz:math_quiz
    ''',
)
