from utils.voiceMonitor import get_vocie_txt

APP_ID = '34426540'
API_KEY = '5HeZfSqX5D5H5lu0tbj7pBfc'
SECRET_KEY = 'Vaz4LZU3jPzcmLgKbYHjb8frxEY7o62x'

if __name__ == '__main__':
    audioTxt = get_vocie_txt(APP_ID, API_KEY, SECRET_KEY)
    print(audioTxt)
