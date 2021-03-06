import setuptools


setuptools.setup(
    name='confluent-data-tools',
    version='0.1.0',

    author='Max Zheng',
    author_email='mzheng@confluent.io',

    description='Data transformation tools',
    long_description=open('README.md').read(),

    url='https://github.com/confluentinc/data-tools',

    install_requires=open('requirements.txt').read(),

    license='Apache License 2.0',

    packages=['confluent'],
    include_package_data=True,

    python_requires='>=3.6',
    setup_requires=['setuptools-git', 'wheel'],

    entry_points={
       'console_scripts': [
           'transform = confluent.data.scripts:transform',
           'bq-admin = confluent.data.scripts:bq_admin',
       ],
    },

    # Standard classifiers at https://pypi.org/classifiers/
    classifiers=[
      'Development Status :: 5 - Production/Stable',

      'Intended Audience :: Science/Research',
      'Topic :: Text Processing',

      'License :: OSI Approved :: Apache Software License',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],

    keywords='data transformation',
)
