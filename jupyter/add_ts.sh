# Jupyter notebook typescript 추가
pkg update -y && pkg upgrade -y
pkg install nodejs -y
npm install -g typescript
npm install -g ts-node
deno jupyter --install
