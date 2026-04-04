# Jupyter notebook에 ruby 추가
pkg update -y && pkg upgrade -y
pkg install ruby -y
gem install iruby
iruby register --force
