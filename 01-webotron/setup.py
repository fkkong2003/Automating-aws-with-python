from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Wilfred Kong',
    author_email='fkkong2003@yahoo.com',
    description='Webotron 80 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    #url='https://github.com/ACloudGuru/automating-aws-with-python/tree/master/01-webotron',
    url='https://github.com/fkkong2003/Automating-aws-with-python',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
