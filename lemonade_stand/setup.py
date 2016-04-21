from setuptools import setup

setup(name='lemonade_stand',
      version='0.1.0',
      packages=['lemonade_stand'],
      entry_points={
          'console_scripts': [
              'lemonade_stand = lemonade_stand.__main__:main'
          ]
      },
      )