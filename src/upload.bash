    
port=/dev/ttyACM0
upload_images=false
upload_single=false

# Get optional flags
while getopts ":if:" opt; do
    echo 'opt = ' $opt
    case $opt in
        i) 
            upload_images=true
        ;;
        f)
            upload_single=true
            upload_single_filename=${OPTARG}
        ;;
    esac
done

echo
echo 'upload options'
echo '--------------'
echo 'upload_images = ' $upload_images 
echo 'upload_single = ' $upload_single
echo

# Upload images if requested
if [ "$upload_images" = true ]; then
    for entry in ./icons/*
    do
        case $entry in 
            *.png)
                echo 'uploading' $entry
                ampy -p $port put $entry
        esac
    done
    exit 0
fi

if [ "$upload_single" = true ]; then
    echo 'uploading' $upload_single_filename
    ampy -p $port put $upload_single_filename
else
    # Upload python files
    for entry in *
    do
        case $entry in 
            *.py)
                echo 'uploading' $entry
                ampy -p $port  put $entry
                ;;
        esac
    done

fi

ampy -p /dev/ttyACM0 reset --hard
tio /dev/ttyACM0
