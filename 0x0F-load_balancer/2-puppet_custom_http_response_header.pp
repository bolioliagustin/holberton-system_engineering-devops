#creating a custom HTTP header response, but with puppet.

exec {'httpd':
    command   => 'sudo apt update;
    sudo apt install -y nginx;
    sudo ufw allow 'HTTP';
    sudo service nginx start;
    sed -i '/location /a \    add_header X-Served-By $hostname;' /etc/nginx/sites-available/default
    sudo service nginx restart;
