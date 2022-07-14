#!/bin/sh

-----------------------------------
# Ubuntuのアップデート
sudo apt update
sudo apt upgrade -y

----------------------------------
# Dockerのインストール
# Docker Enginをインストール

# 1, Docker公式GPG鍵を追加
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 2, Docker安定板のリポジトリを追加
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 3, リポジトリをアップデートし、Docker Engineをインストール
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y

# 4, docker-composeもインストール
sudo apt install docker-compose -y

----------------------------------
# Dockerの準備

# Dockerデーモンを起動
sudo service docker start

# ユーザーをDockerグループに追加
sudo gpasswd -a "$USER" docker
