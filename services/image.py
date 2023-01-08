'''
Service handles image uploads with imgur API.
'''
import requests
from io import BytesIO


class Image:
    '''
    Class definition with methods and properties for handling X-lease images
    '''

    def upload(image_file=None, path=""):
        '''
        File upload method stores device display images on imgur server
        '''
        url = "https://api.imgur.com/3"
        headers = {"Content-Type": "multipart/form-data"}
        print(type(image_file))
        if image:
            data = {'image': image_file}
        elif path:
            data = {'image': open(path, 'rb')}
        try:
            response = requests.post("{}/upload".format(url),
                                     headers=headers,
                                     files=data)
        except Exception as e:
            print(e)
        else:
            data = response.json()
            print(data)
            return data['link']
