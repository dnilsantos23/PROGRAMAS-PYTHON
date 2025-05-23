from cefpython3 import cefpython as cef
import platform
import sys
def main():
    check_versions()
    sys.excepthook = cef.ExceptHook # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url=" https://www.google.com/",window_title="Olá, mundo! Este é o primeiro exemplo do CEF python") 
    cef.MessageLoop() 
    cef.Shutdown()

def check_versions(): 
    ver=cef.GetVersion()
    print("[hello_world.py] CEF python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] python {ver}{arch}".format(ver=platform.python_version(),arch=platform.architecture()[0])) 
    assert cef.__version__>= "66.1", "CEF python v57.0+ required to run this"


if __name__ == '__main__':
    main()