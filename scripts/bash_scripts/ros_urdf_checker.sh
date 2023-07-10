

echo "Directory to search for urdf files:"
read URDF_DIR

RES_FILENAME=urdf_checker.txt
rm $URDF_DIR/$RES_FILENAME

URDF_FILES=$(find $URDF_DIR -mindepth 0 -type f -iname "*.urdf")

# echo "urdf files: $URDF_FILES"

for FILE in $URDF_FILES
do
  # echo $FILE
  echo "-------------------------------------------------------------------" >> $URDF_DIR/$RES_FILENAME
  echo "Filename: $FILE" >> $URDF_DIR/$RES_FILENAME 2>&1
  echo  >> $URDF_DIR/$RES_FILENAME
  check_urdf $FILE -a >> $URDF_DIR/$RES_FILENAME 2>&1
  echo  >> $URDF_DIR/$RES_FILENAME
  echo  >> $URDF_DIR/$RES_FILENAME
  # check_urdf $FILE | tee -a $URDF_DIR/$RES_FILENAME
done


