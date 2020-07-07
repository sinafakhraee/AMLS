# Instructions on how to use VSC to develop remotely (e.g. on azure machine learning compute instace)

1. install Remote - SSH frrom the VC Extentions Marketplace <br>
![picture](./images/remote-ssh-plugin-install.PNG)<br>
2. click lower left hand corner of VC to connect <br>
![picture](./images/click-to-connect.PNG)<br>
3. select Remote-SSH: Connect to Host <br>
![picture](./images/connect-to-host.PNG)<br>
4. select Configure SSH Hosts... <br>
![picture](./images/configure-ssh-host.PNG)<br>
5. select local ssh config file (e.g. c\user\username\.ssh\config)  <br>
![picture](./images/config_ssh_config_file.PNG)<br>
6. update the config file <br>
![picture](./images/update-ssh-config-file.PNG)<br>
7. generate ssh public/private key pair <br>
![picture](./images/generate-ssh-key.PNG)<br>
8. go to AML portal and create a ssh-enabled compute instance. make sure to copy and paste your generated public key into the SSH public key box <br>
![picture](./images/create-compute-instance-ssh-enabled.PNG)<br>
9. get the SSH details (e.g. hostname, user, port) and update config file in step 6 <br>
![picture](./images/get-ssh-details.PNG)<br>
