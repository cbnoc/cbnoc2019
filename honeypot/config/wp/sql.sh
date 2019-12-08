ADDRESS_MGMT=10.1.1.32
ADDRESS_UNSECURE=$(ip -f inet -o addr show ens192 |cut -d\  -f 7 | cut -d/ -f 1)

DB_NAME=wordpress
UPDATE_URI="UPDATE wp_options SET option_value = 'http://$ADDRESS_UNSECURE' WHERE option_name='siteurl' OR option_name='home';"

mysql -h $ADDRESS_MGMT -u $MYSQL_USER -p $DB_NAME --password=$MYSQL_PASSWORD -e "$UPDATE_URI"
# mysql -h $ADDRESS_MGMT -u $MYSQL_USER -p $DB_NAME --password=$MYSQL_PASSWORD -e "select * from wp_options where option_name='siteurl' OR option_name='home'"
