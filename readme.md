### Clocker - Console Alarm Clock
This is a project that provides console alarm clock. There's nothing especially hard. All that you have to do is - start main file.

```
./alarm.py hh:mm
```

This script sets alarm at next hh:mm time from current time moment. Particulary it means that you can not set up alarm at more than 24h time interval without code modifying. (Maybe will be added later)

All ringtones you want to be able to set up as an alarm ringtone must be placed in folder `ringtones`

This script uses python-vlc library. You should be sure that you have newest version of VLC and `python-vlc` lib (can be downloaded from pip)

Have fun and write your improvement suggestions in issues ;)