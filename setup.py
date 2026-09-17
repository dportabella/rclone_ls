from setuptools import setup

version = "0.0.3"

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    'rclone>=2.0.0',
    'humanize>=4.6.0'
]

setup(
    name='rclone_ls',
    version=version,
    description='Script to list files/dirs and their sizes in a given rclone path.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/dportabella/rclone_ls',
    author='David Portabella',
    author_email='david.portabella@gmail.com',
    license='MIT',
    python_requires='>=3.0',
    py_modules=['rclone_ls_full'],
    entry_points={'console_scripts': ['rclone_ls_full = rclone_ls_full:main']},
    include_package_data=True,
    install_requires=requirements,
    keywords=[
        "Python",
        "rclone",
        "ls",
    ],
)
