from setuptools import setup


VERSION = '1.0'

install_requires = [
    'pytest>=3.5.1',
    'pytest-rerunfailures>=4.1',
    'allure-pytest>=2.5.0',
    'allure-python-commons>=2.5.0',
    'pytest-xdist>=2.1.0',
    'selenium>=3.141.0',
    'chromedriver>=2.24.1',
    'pytest-html>=2.1.1'
]


def main():
    setup(
        name='Python selenium pytest one.com',
        version=VERSION,
        description='Pytest testing framework using selenium',
        author='yasser',
        url='https://github.com/yasserfaraazkhan/Selenium-Python-Pytest.git',
        install_requires=install_requires
    )


if __name__ == '__main__':
    main()
