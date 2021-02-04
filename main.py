import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#using an ipv4 connection and its going to scan tcp
s.settimeout(5)


def port_scanner(host, port):
    if s.connect_ex((host, port)):
        print("error-port is closed")
    else:
        print("The port is open")


def main():
    ip = input("Enter an ip")#Takes the input and sets it as the ip...It has to be string due to the ip format
    port = int(input("Enter a port"))#sets the input as port and its converted to int otherwise it would be a string and this will throw up an error

    port_scanner(ip, port)


if __name__ == "__main__":
    main()