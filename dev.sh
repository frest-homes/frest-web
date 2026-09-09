#!/bin/sh
# Local preview build. Keeps site/img (2 minutes to regenerate) and wipes everything else.
set -e
LANG_ROOT=${1:-lv}
mkdir -p site/img
find site -mindepth 1 -maxdepth 1 ! -name img -exec rm -rf {} +
python3 build.py --base /frest-web/ --root-lang "$LANG_ROOT" "$@"
rm -rf serve/frest-web && mkdir -p serve && cp -r site serve/frest-web
echo "serving http://localhost:8765/frest-web/  (root lang $LANG_ROOT)"
