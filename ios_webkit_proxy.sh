#!/bin/bash


osascript -e 'tell app "Terminal"
    do script "ios_webkit_debug_proxy -c db55c238e873230ee454c54a63724397a2981acd:27753"
end tell'
