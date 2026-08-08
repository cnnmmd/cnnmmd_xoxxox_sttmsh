#!/bin/bash

pthtop="$(cd "$(dirname "${0}")/../../../.." && pwd)"
source "${pthtop}"/manage/lib/params.sh
source "${pthtop}"/manage/lib/shared.sh
source "${pthcrr}"/params.sh

pthapp="${pthsrc}"/appmsh
namsrv='xoxxox_sttmsh'
lngtgt='ja'

addimg ${imgtgt} "${cnfimg}" "${pthdoc}"
test -d "${pthapp}" || mkdir "${pthapp}"
if cd "${pthapp}"
then
  test -d msh || mkdir msh
  test -d msh/download.moonshine.ai || \
  docker compose -f "${cnfcmp}" run --rm ${namsrv} /env/python/bin/python3 -m moonshine_voice.download --stt --language ${lngtgt}
fi
