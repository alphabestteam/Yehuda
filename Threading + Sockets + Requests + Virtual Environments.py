import requests
import time
import threading

# 1. threads are wires that work at the same time on the code
# 2. import threading
# 3. send HTTP requests , socket is low level and requests  is higher level and more functionality


def main():
    print("main")


def cal_time(t):
    def result(*args, **kwargs):
        start = time.time()
        t(*args, **kwargs)
        end = time.time()
        print("is take to us : ", end - start, "sec")
    return result


@cal_time
def downloading_file():
    def get_url(url, name_picture):
        x = requests.get(url)
        open(f"{name_picture}.ico", 'wb').write(x.content)

    get_url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png', "matzov")
    get_url('https://github.githubassets.com/images/modules/open_graph/github-mark.png', "github")
    get_url('https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png', "gmail")
    get_url('https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png', "google")


@cal_time
def arr_downloading_file():
    urls = ['https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png',
            'https://github.githubassets.com/images/modules/open_graph/github-mark.png',
            'https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png',
            'https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png'
            ]

    def get_url(url, name_picture):
        x = requests.get(url)
        open(f"{name_picture}.ico", 'wb').write(x.content)

    for i in range(len(urls)):
        get_url(urls[i], i)


@cal_time
def Threading_downloading_file():
    urls = ['https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png',
            'https://github.githubassets.com/images/modules/open_graph/github-mark.png',
            'https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png',
            'https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png'
            ]

    def get_url(url, name_picture):
        x = requests.get(url)
        open(f"{name_picture}.ico", 'wb').write(x.content)

    t1 = threading.Thread(target=get_url(urls[0], 1), name='t1')
    t2 = threading.Thread(target=get_url(urls[1], 2), name='t2')
    t3 = threading.Thread(target=get_url(urls[2], 3), name='t3')
    t4 = threading.Thread(target=get_url(urls[3], 4), name='t4')

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("using thread")

# locks are locks code until is finish to not cues problem with threads


if '__main__' == __name__:

    downloading_file()
    arr_downloading_file()
    Threading_downloading_file()

#####################################################################################################

# socket is connect two computer on the network , we not always wont to use socket because is low level
# u can use SocketCluster
# is the sever in the middle and around him is the clients
# 1 the server execute and wait for request
# 2 the client begin the conversation first
# 3 the server response to the client requests
# 4 client will shut up and say bye and the server shut up

# socket(socket.AF_INET, socket.SOCK_STREAM) AF_INET is the address ip , SOCK_STREAM is the TCP protocol.


#####################################################################################################

# 1 virtual environments came to solve when you wont to change version and do a lot of change and not to ruin your pc
# for example do you wont chang version on python to 3.8 or models
# 2 is take some memory and use that for the virtual
# 3 first we install it pip3 install virualenv , make new dir  virtualenv myVirtualEnv , and now we start source ./myVirtualEnv/bin/activate and done you have virtual in you pc

# 4 no , i need to download the file agin
