# DALETWEBGO #

This is for now a private test project for me to get familuar with Django and concepts.

The concept for the whole "playground" is to have a frontend to select wav.files (eventually might be integrated to query Dalet/radio software for them).
Once selected it will automaticly go through a series of stages to actually process these files, the (optional steps will probably not be made in a while):

* (Optional) Get the file listings from Dalet instead of folder.
* (Optional) Get the metadata from Dalet and use it to get proper MP3 tags
* Encode the chosen wav file to mp3, verify everything ok.
* Move the encoded mp3 to a ftp site automaticly, verify size and if possible checksum.
* (Optional) Interface with a shared table with wordpress external db to add data about publised files to make them easily retrievable from the web interface.


The plan is to use a queue manager to do the actual processing with the Django framework beeing on top for a pretty light user interface.
Ideally there would be retry functionality and detailed easy logs of what failed and why. Also ideally a few retries before giving up on a queue item.
As I'm pretty new to this plan might change drasticly before I'm done.
