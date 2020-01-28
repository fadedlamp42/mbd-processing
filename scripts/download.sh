echo "     creating/refreshing raw/"
rm -rf raw
mkdir raw
cd raw
echo

echo "     downloading"
wget http://mindbigdata.com/opendb/MindBigData-MW-v1.0.zip
wget http://mindbigdata.com/opendb/MindBigData-EP-v1.0.zip
wget http://mindbigdata.com/opendb/MindBigData-MU-v1.0.zip
wget http://mindbigdata.com/opendb/MindBigData-IN-v1.06.zip
echo

echo "     extracting"
unzip MindBigData-EP-v1.0.zip
unzip MindBigData-MU-v1.0.zip
unzip MindBigData-MW-v1.0.zip
unzip MindBigData-IN-v1.06.zip
mv EP1.01.txt EP.txt
echo

echo "     cleaning"
rm *.zip
