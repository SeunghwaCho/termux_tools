# Jupyter Notebook 설치
pkg update -y && pkg upgrade -y

export ANDROID_API_LEVEL=$(getprop ro.build.version.sdk)
echo "export ANDROID_API_LEVEL=$(getprop ro.build.version.sdk)" >> ~/.bashrc
source ~/.bashrc

pkg install -y tmux
pkg install -y python rust libffi clang make cmake git libbz2 zlib libjpeg-turbo
pkg install -y binutils
pkg install -y python-psutil
CFLAGS="-I$PREFIX/include" LDFLAGS="-L$PREFIX/lib" pip install --no-cache-dir --force-reinstall cffi

pip install --upgrade pip setuptools wheel
pip install --no-cache-dir jupyter

python add_to_bashrc.py
source ~/.bashrc
