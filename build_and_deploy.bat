echo off
echo ==== Installing npm dependencies ====
call npm i
echo ==== Building distribution ====
call npm run build
echo ==== Transfering dist/ to /var/www/hegardt.se/html/ at 134.209.240.67 ====
scp -r "dist/*" root@134.209.240.67:/var/www/hegardt.se/html/
echo ==== Adding execution permission to files ====
ssh root@134.209.240.67 sudo chmod -R 755 /var/www/hegardt.se
echo ==== Restarting Nginx ====
ssh root@134.209.240.67 sudo systemctl restart nginx
