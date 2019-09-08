# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonautomation')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='kongvideolyzervideos',CreateBucketConfiguration={'LocationConstraint': session.region_name})
from pathlib import Path
get_ipython().run_line_magic('ls', '/Users/Admin/Downloads/*.mp4')
get_ipython().run_line_magic('ls', '~/Users/Admin/Downloads/*.mp4')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('ls', '~\\Downloads\\*.mp4')
get_ipython().run_line_magic('ls', '~/Downloads/*.mp4')
get_ipython().run_line_magic('cd', '~/Downloads')
get_ipython().run_line_magic('ls', '*.mp4')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('ls', '\\Users\\Admin\\Downloads\\*.mp4')
pathname = '~\Downloads\Pexels Videos 2364207.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
pathname = '~\Downloads\Pexels Videos 2364297.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object':{'Bucket':bucket.name, 'Name':path.name}})
