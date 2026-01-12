echo "HELLO AWS!" | sudo tee /var/www/html/index.html
close
exit
sudo yum update -y
sudo yum install httpd -y
sudo systemctl httpd
sudo systemctl start httpd
systemctl enable httpd
sudo systemctl enable httpd
"Hello AWS!" | sudo tee /var/www/html/index.html
echo "Hello AWS!" | sudo tee /var/www/html/index.html
exit
sudo amazon-linux-extras install nginx1 -y
echo "<h1>Hello from AWS EC2</h1>" | sudo tee /usr/share/nginx/html/index.html
mkdir /usr/share/nginx/html/index.html
mkdir /usr/share/nginx/html/
sudo dnf install nginx -y
sudo systemctl start nginx
sudo lsof -i :80
sudo systmctl stop httpd
sudo systemctl stop httpd
sudo systemctl disable httpd
sudo systemctl start nginx
sudo systermctl status nginx
sudo systemctl status nginx
"<html><body><h1>나의 첫 EC2 호스팅 성공</h1><p>이제 외
부에서도 이 페이지를 볼 수 있습니다.</p></body></html>" | sudo tee /usr/share/nginx/html/index.html
echo "<html><body><h1></h1><p>이제 외
부에서도 이 페이지를 볼 수 있습니다.</p></body></html>" | sudo tee /usr/share/nginx/html/index.html
echo "<html><body style='text-align:center; padding-top:50px;'><h1>My First AWS EC2 Hosting Success</h1><p>Your Nginx server is running perfectly on AWS.</p></body></html>" | sudo tee /usr/share/nginx/html/index.html
echo "<html><body style='text-align:center; padding-top:50px;'><h1>My First AWS EC2 Hosting Success</h1><p>Your Nginx server is running perfectly on AWS. -SoYoung-</p></body></html>" | sudo tee /usr/share/nginx/html/index.html
echo "<html><body style='text-align:center; padding-top:50px;'><h1>My First AWS EC2 Hosting Success</h1><p>Your Nginx server is running perfectly on AWS. -SOYOUNG-</p></body></html>" | sudo tee /usr/share/nginx/html/index.html
aws s3 cp s3://your-bucket-name/folder/file.txt .
aws s3 cp s3://soyoung-bucket-0109/folder/file.txt .
aws s3 ls s3://soyoung-bucket-0109/folder/
aws s3 ls s3://soyoung-bucket-0109/
aws s3 cp s3://soyoung-bucket-0109/test.txt .
aws s3 ls s3://soyoung-bucket-0109/ --recursive
aws s3 cp s3://soyoung-bucket-0109/b.txt .
aws s3 ls s3://soyoung-bucket-0109/ --recursive
aws s3 cp "s3://soyoung-bucket-0109/git 교안.zip" .
aws s3 cp my_script.sh s3://soyoung-bucket-0109/
aws s3 sync . s3://soyoung-bucket-0109/
aws s3 ls s3://soyoung-bucket-0109/ --recursive
aws s3 sync . s3://soyoung-bucket-0109/
aws s3 ls s3://soyoung-bucket-0109/
ls -lh
aws s3 ls s3://soyoung-bucket-0109/ --recursive
exit
echo "aaa" >> b.txt
ls
cat b
cat b.txt 

cat b.txt 
aws s3 ls
aws s3 ls s3://soyoung-bucket-0129,git/
aws s3 ls s3://soyoung-bucket-0129
aws s3 ls s3://soyoung-bucket-0129/
aws s3 ls s3://soyoung-bucket-0109/
aws s3 cp b.txt s3://soyoung-bucket-0109
aws s3 ls s3://soyoung-bucket-0109/
aws s3 cp C:\Users\SY\Downloads\test.txt s3://soyoung-bucket-0109
aws s3 cp "C:\Users\SY\Downloads\test.txt.txt" s3://soyoung-bucket-0109
aws s3 cp "C:\Users\SY\Downloads\test.txt" s3://soyoung-bucket-0109
aws s3 cp "C:\Users\SY\Downloads\test.txt" s3://soyoung-bucket-0109/
aws s3 cp C:\Users\SY\Downloads\test.txt s3://soyoung-bucket-0109/
aws s3 ls
aws s3 website s3://soyoung-bucket-0109/ --index-document index.html --error-document error.html
aws s3api put-public-access-block `
    --bucket my-bucket-name `
    --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
aws s3api put-public-access-block --bucket my-bucket-name --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
aws s3api put-bucket-policy --bucket my-bucket-name --policy file://policy.json~
aws s3api put-public-access-block --bucket my-bucket-name --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
aws s3api put-bucket-policy --bucket my-bucket-name --policy file://policy.json~
aws sts get-caller-identity
--bucket soyoung-bucket-0109
--bucket my-bucket
aws s3api put-public-access-block --bucket 본인-버킷-이름 --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
aws s3api put-public-access-block --bucket soyoung-bucket-0109 --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
aws s3api put-bucket-policy --bucket soyoung-bucket-0109 --policy file://policy.json
ls policy.json
sudo yum update -y
sudo amazon-linux-extras insatall nginx1 -y
sudo amazon-linux-extras install nginx1 -y
sudo systemctl start nginx
