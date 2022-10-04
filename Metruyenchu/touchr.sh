#!/usr/bin/env bash

function touchr() {
    # take .extension
    if [[ $1 == *.py ]]; then
        echo '#!/usr/bin/env python3' > $1
    elif [[ $1 == *.sh ]]; then
        echo '#!/usr/bin/env bash' > $1
    else
        echo > $1
    fi

    # [[ "$1" == *.py ]] && echo '#!/usr/bin/env python3' > $1 && return
    # [[ "$1" == *.sh ]] && echo '#!/usr/bin/env bash' > $1 && return
    # [ "$*" = *.py ] && echo 'true'
    # [ -z "$*" ] && echo 'false'
    
}

touchr $1
