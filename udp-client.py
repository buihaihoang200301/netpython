import socket

if __name__ == "__main__":
    host ="10.10.15.28"
    port = 1234
    addr =(host,port)

    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        data = input("Enter: ")

        if data =="!EXIT":
            data = data.encode("utf-8")
            client.sendto(data,addr)
            print("Disconnected")
            break
        
        data=data.encode("utf-8")
        client.sendto(data,addr)
        data,addr = client.recvfrom(1024)
        data = data.decode("utf-8")
        print(f"Send to server: {data}")
