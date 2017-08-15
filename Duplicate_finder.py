import sys
import os
import hashlib

def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes = {}
    flag=0
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                hashobj = hash()
                for chunk in chunk_reader(open(full_path, 'rb')):
                    hashobj.update(chunk)
                file_id = (hashobj.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id)
                if duplicate:
                    print "Duplicate(s) found for %s " % full_path
                    hashes[file_id].append(full_path)
                    flag=1
                else:
                    hashes[file_id] = [full_path]
    if flag==0 :
        print "No duplicates found"
        print '-'*25
        return;
    for key in hashes:
        numDuplicates= len(hashes[key])
        if numDuplicates>1:
            print '-'*25
            for x in range(numDuplicates):
                print str(x+1) +'. ' +hashes[key][x]
            print '-'*25
            print 'Do you wish to delete any duplicates? (y/n)'
            print '-'*25
            inp=raw_input()
            if inp=='n' or inp=='N':
                continue
            elif inp=='y' or inp=='Y':
                toDelete=raw_input('Input index number(s) of the duplicate(s) to delete as comma seperated values: ').split(',')
                for num in toDelete:
                    os.remove(hashes[key][int(num)-1])
    print 'End of list'

if sys.argv[1:]:
    check_for_duplicates(sys.argv[1:])

else:
    print "Please pass the paths to check as parameters to the script"
