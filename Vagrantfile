Vagrant.configure("2") do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/trusty64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"
  # config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
    config.vm.synced_folder "testing", "/home/vagrant/testing"
  #    , type: "rsync", rsync_exclude: ".git/"
  
  config.vm.network :forwarded_port, guest:4444, host:4444
  # config.vm.network :forwarded_port, guest:80, host:80
  # config.vm.network :forwarded_port, guest:443, host:443
  config.vm.provision "shell" do |s|
    s.path = "setup.sh"
  end
  config.vm.provider :virtualbox do |vb|
      vb.name = "testing"
      vb.gui = true
   end
end
