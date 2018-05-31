from .helper_functions import *


def use_brian_login():
    user = 'brian'
    # Alternative approach:
    # password = open("/Users/briancohn/Desktop/password.txt").read()
    try:
        os.environ["MY_PASSWORD"]
    except KeyError:
        print("Please set the environment variable MY_PASSWORD")
        sys.exit(1)
    password = os.environ["MY_PASSWORD"]
    print("MARK")
    # print(password)
    ftp = connect(user, password)
    return(ftp)


class TestClass(object):
    def test_working_dir_acq(self):
        ftp = use_brian_login()
        ftp.retrlines('LIST home')
        ftp.quit()
        ftp = None

    def test_upload(self):
        ftp = use_brian_login()
        # Upload big file
        p = os.path.abspath(os.path.dirname(__file__))
        input_filepath = p + "/helper_functions.py"
        destination_filepath = "home/brian_scratch/helper_functions_remote.py"
        tx_with_progress(ftp, input_filepath, destination_filepath,
                         block_size_bytes=12500000)
        ftp.quit()
        ftp = None

    def test_download(self):
        filepath_pensieve = "home/brian_scratch/helper_functions_remote.py"
        p = os.path.abspath(os.path.dirname(__file__))
        filepath_local = p + "/helper_functions_prime.py"
        if os.path.isfile(filepath_local):
            os.remove(filepath_local)

        ftp = use_brian_login()
        # Download that file back to local
        # Make sure the local file doesn't exist before the download
        # script is run.

        receive(ftp, filepath_pensieve, filepath_local,
                block_size_bytes=12500000)
        ftp.quit()
        ftp = None
        assert os.path.isfile(filepath_local)
        os.remove(filepath_local)
        assert os.path.isfile(filepath_local) is False
