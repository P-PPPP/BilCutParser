import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name="BilCutParser",
  version="0.0.1",
  author="PPPPP",
  author_email="ppzzhh1186861238@hotmail.com",
  description="Parse BiliBili Xml FIle To Srt File",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/P-PPPP/BilCutParser",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "Operating System :: OS Independent",
  ],
)