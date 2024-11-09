from setuptools import setup, find_packages

setup(
    name='math_quiz',                # Name of your package
    version='0.1',                   # Initial version
    packages=find_packages(),        # Automatically find packages in the directory
    install_requires=[               # Dependencies listed here or in `requirements.txt`
        # List dependencies if needed, or refer to requirements.txt
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',   # Allows running `math_quiz` from the command line
        ],
    },
    description='A simple math quiz application',  # Brief description
    author='Mariam Aly',                 # Your name
    author_email='aly.mariamkh@gmail.com',   # Your email
    url='https://github.com/mariamhanafy02/dsss_homework_2',  # Link to your repo
    classifiers=[
        'Programming Language :: Python :: 3.9.19',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
    ],
)
