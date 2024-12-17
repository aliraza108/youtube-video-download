from pytube import YouTube 

# where to save 
SAVE_PATH = "/home/chintusharma/Downloads" #to_do 

# link of the video to be downloaded 
link = "https://www.youtube.com/watch?v=a7baAGCBA9U&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg"

try: 
    # object creation using YouTube 
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

# Get all streams and filter for mp4 files
mp4_streams = yt.streams.filter(file_extension='mp4').all()

# get the video with the highest resolution
d_video = mp4_streams[-1]

try: 
    # downloading the video 
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except: 
    print("Some Error!")


    # with open('python.csv', newline='') as csvfile:
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         url = row[0]
    #         if url:  # Skip empty lines
    #             download_youtube_video(url)
