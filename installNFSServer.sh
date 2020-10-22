source config/nfs.cfg

sudo apt-get update -y
sudo apt-get install nfs-kernel-server -y

sudo mkdir -p $nfsDir

echo "$nfsDir $serverIP(rw,no_root_squash)" | sudo tee -a /etc/exports
