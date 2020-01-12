#!/bin/bash
DIR=$1
function check_user_args() {
  if [ -z "$DIR" ]
    then
      echo "please provide directory to check"
      exit 1
    else
      if [ ! -d "$DIR" ]
        then
          echo "Error: Directory $DIR does not exists."
          exit 1
      fi
  fi
}

function rename_files() {
  for f in "$DIR"/*; do
    if [ -f "$f" ]; then
      if [ $(basename "${f}") == 'cat.txt' ]
        then
          echo "found a cat"
          mv $f "$DIR/old_cat.txt"
      fi
      if [ $(basename "${f}") == 'dog.txt' ]
        then
          echo "found a dog"
          mv $f "$DIR/old_dog.txt"
      fi
    fi
  done
}

check_user_args
rename_files
echo "Done :)"