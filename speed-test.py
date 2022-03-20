#!/usr/bin/python
import speedtest
from colors import Colors

test = speedtest.Speedtest()

print(Colors.OKBLUE + "Loading Server list ....")
test.get_servers()
print(Colors.OKBLUE + "Choosing best Sever ....")
best = test.get_best_server()
print(Colors.OKGREEN + f"Found: {best['host']} located in {best['country']}")

print(Colors.OKBLUE + "Performing Download Test ...")
download_result = test.download()
print(Colors.OKBLUE + "Performing Upload Test ...")
upload_result = test.upload()
ping_result = test.results.ping

print(Colors.OKGREEN + f"DOWNLOAD SPEED : {download_result / 1024 / 1024:.2f} Mbits/Second")
print(Colors.OKGREEN + f"UPLOAD SPEED : {upload_result / 1024 / 1024:.2f} Mbits/Second")
print(Colors.OKGREEN + f"Ping : {ping_result:.2f} ms")
