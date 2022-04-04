import speedtest
speed = speedtest.Speedtest()
download_speed = speed.download()
upload_speed = speed.upload()
print('The download speed is {download_speed }' )
print('The upload speed is {upload_speed }' )
