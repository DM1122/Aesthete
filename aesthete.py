import os
from google_images_download import google_images_download as gid

directory = "music"

if __name__ == "__main__":


    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            filepath = os.path.join(directory, filename)
            query = os.path.splitext(filename)[0]
            print(query)

            response = gid.googleimagesdownload() # class instantiation

            arguments = {
                "keywords": query,
                "limit": 4,
                "print_urls": True,
                }

            absolute_image_paths = response.download(arguments)
            paths = response.download(arguments)
