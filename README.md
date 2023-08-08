## Deploy backend
### 1. Installation
#### 1.1. Install dotnet 7.0 [(Reference)](https://learn.microsoft.com/en-us/dotnet/core/install/linux-centos)
* Check dotnet installed
```
dotnet --list-sdks
dotnet --list-runtimes
```
* Run commands:
```
sudo rpm -Uvh https://packages.microsoft.com/config/centos/7/packages-microsoft-prod.rpm
```
```
sudo yum install dotnet-sdk-7.0
```

#### 1.2. Install mongodb [(Reference)](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-amazon/)
* Configure the package management system

    Create file in `/etc/yum.repos.d/mongodb-org-6.0.repo`
```
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
```

* Install the MongoDB packages
```
sudo yum install -y mongodb-org
```

* Start mongodb service
```
sudo systemctl start mongod
```
* Import mongo data

Open mongosh
```
mongosh
```

  Select database VoucherParadise
```
use VoucherParadise
```

Import data
```
 mongosh --file .\db_creation.js
```

#### 1.3. Install tmux [(Reference)](https://tmuxcheatsheet.com/)

Install tmux
```
 sudo yum install tmux
```

Create session
```
tmux new -s voucher_api
```

#### 1.4. Install git & clone code
```
sudo yum install git
```

cd to folder `/home/ec2-user/voucher-paradise`

Start ssh agent `$ eval "$(ssh-agent -s)"`

Add ssh key to session `ssh-add ~/keys/thanhvietle2017`

Clone project
```
git clone https://github.com/vietthanhle89/voucher_paradise.git
```
cd to folder `voucher_paradise` and switch to `main` branch


### 2. Deploy
Open terminal and attach to tmux session
```
 tmux attach -t voucher_api
```
cd to folder `/home/ec2-user/voucher-paradise/voucher_paradise/VoucherParadiseAPI`

Run command line
```
dotnet run
```

## Deploy frontend
### 1. Installation
#### 1.1. Install nginx
```
sudo amazon-linux-extras install nginx1
```

#### 1.2. Config nginx
- cd to folder `/etc/nginx`

- Run command to open `nginx.conf` file
```
sudo vi nginx.conf
```

- Create folder `/usr/share/nginx/voucher_admin`

Set permission folder `voucher_admin`
```
sudo chmod -R 755 voucher_admin/
```

- Add new config `server` for new site
```
server {
      listen       10000;
      listen       [::]:10000;
      index index.html;

      location / {
          root /usr/share/nginx/voucher_admin;
          try_files $uri /index.html;
      }
}
```

- Reload nginx config
```
sudo service nginx reload
```

### 2. Build angular
#### 2.1. Change url api
- if want to build angular app for another IP, need to change `apiUrl` in file `environment.prod.ts`
```
export const environment = {
    production: true,
    apiUrl: 'http://18.232.153.220:5555/api'
};

```
#### 2.2. Build angular
In root project angular `VoucherParadiseAdmin` run command:
```
npm run build:prod
```

#### 2.3. Deploy
After build successful, using any tools (FileZilla, WinSCP,...) or command (scp) to copy file build from local to folder `/usr/share/nginx/voucher_admin`.
