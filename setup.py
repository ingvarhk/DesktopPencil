from distutils.core import setup
setup(
  name = 'DesktopPencil',
  packages = ['DesktopPencil'],
  version = '0.3',
  license='MIT',
  description = 'Draw images on top of everything',
  author = 'Ingvar Hahn Kristensen',                   # Type in your name
  author_email = 'ingvar@hahnkristensen.dk',      # Type in your E-Mail
  url = 'https://github.com/ingvarhk/DesktopPencil',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ingvarhk/DesktopPencil/archive/v_02.tar.gz',    # I explain this later on
  keywords = ['Draw', 'Desktop', 'Image'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pywin32',
          'Pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)