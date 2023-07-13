import speedtest

test = speedtest.Speedtest()

print("Loading Server List....")
test.get_servers() #Get list of servers available for speedtest
print("choosing best server.....")
best = test.get_best_server
print(f"Found: {best['host']} located in {best['country']}")

print("performing download test...")
download_result = test.download()

print("performing upload test...")
upload_result = test.upload()
ping_result = test.results.ping

print(upload_result)
print(download_result)
print(ping_result)