# KHE Event Data

## Dump DB to File

```bash
ssh root@khe.io

# Work in /tmp to use less space
cd /tmp

# Export databases
mongodump --db kenthackenough2019

exit
```

## Pull Dump to Desktop

```bash
# Mount server directory to desktop
sshfs root@khe.io:/tmp/<dump-folder> ./remote-mount

# Copy all dump files to this desktop
cp -R * ./local/dumps

# Unmount server
umount ./remote-mount
```

## Convert Dump to JSON

```bash
# ===== Terminal 1. =====
#   Run mongo docker. Don't close.
docker run --name khe-data mongo

# ===== Terminal 2. =====
#   Move dump to container
docker cp ./local/dumps khe-data:/home/dumps

#   Enter docker container
docker exec -it khe-data bash

#   Go to dump files
cd /home/dumps

#   Load dump into Mongo
mongorestore --db kenthackenough2019 kenthackenough2019

#   Export to json
mongoexport -d kenthackenough2019 -c users --jsonArray -o users.json

#   Exit docker container
exit

#   Pull json
docker cp khe-data:/home/dumps/kenthackenough2019/users.json ./local/khe-data

#   Stop the docker container
docker stop khe-data

# Now able to exit Terminal 1.
```

## Cleaning KHE Data
