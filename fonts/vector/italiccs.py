WIDTH = 24
HEIGHT = 24
FIRST = 0x20
LAST = 0x7f

_font =\
b'\x00\x4c\x58\x0e\x4e\x56\x52\x4b\x51\x4c\x52\x53\x53\x4c\x52'\
b'\x4b\x20\x52\x52\x4c\x52\x4f\x20\x52\x52\x56\x51\x57\x52\x58'\
b'\x53\x57\x52\x56\x0d\x4e\x56\x52\x4f\x51\x50\x52\x51\x53\x50'\
b'\x52\x4f\x20\x52\x53\x57\x52\x58\x51\x57\x52\x56\x53\x57\x53'\
b'\x59\x51\x5b\x0b\x4b\x59\x52\x4b\x4e\x5c\x20\x52\x56\x4b\x52'\
b'\x5c\x20\x52\x4e\x51\x57\x51\x20\x52\x4d\x56\x56\x56\x21\x4b'\
b'\x5a\x51\x48\x51\x5c\x20\x52\x54\x48\x54\x5c\x20\x52\x57\x4c'\
b'\x56\x4c\x56\x4d\x57\x4d\x57\x4c\x55\x4b\x50\x4b\x4e\x4c\x4e'\
b'\x4e\x4f\x50\x56\x53\x57\x54\x20\x52\x4e\x4e\x4f\x4f\x56\x52'\
b'\x57\x54\x57\x56\x56\x57\x54\x58\x51\x58\x4f\x57\x4e\x56\x4e'\
b'\x55\x4f\x55\x4f\x56\x4e\x56\x19\x4a\x5a\x58\x4b\x4c\x58\x20'\
b'\x52\x4f\x4b\x50\x4c\x50\x4e\x4f\x4f\x4d\x4f\x4c\x4e\x4c\x4c'\
b'\x4d\x4b\x4f\x4b\x53\x4c\x56\x4c\x58\x4b\x20\x52\x55\x54\x54'\
b'\x55\x54\x57\x55\x58\x57\x58\x58\x57\x58\x55\x57\x54\x55\x54'\
b'\x28\x4a\x5b\x59\x50\x58\x50\x58\x51\x59\x51\x59\x50\x58\x4f'\
b'\x57\x4f\x56\x50\x55\x54\x54\x56\x53\x57\x51\x58\x4f\x58\x4d'\
b'\x57\x4c\x56\x4c\x54\x4d\x53\x4f\x52\x52\x50\x53\x4e\x53\x4c'\
b'\x52\x4b\x50\x4b\x4f\x4c\x4f\x4e\x50\x51\x55\x57\x57\x58\x58'\
b'\x58\x59\x57\x20\x52\x4f\x58\x4d\x56\x4d\x54\x4f\x52\x20\x52'\
b'\x4f\x4e\x50\x50\x56\x57\x57\x58\x07\x4e\x56\x53\x4c\x52\x4d'\
b'\x51\x4c\x52\x4b\x53\x4c\x53\x4e\x51\x50\x0f\x4d\x57\x55\x48'\
b'\x53\x4a\x51\x4d\x50\x50\x50\x54\x51\x57\x53\x5a\x55\x5c\x20'\
b'\x52\x53\x4a\x52\x4c\x51\x50\x51\x54\x52\x58\x53\x5a\x0f\x4d'\
b'\x57\x4f\x48\x51\x4a\x53\x4d\x54\x50\x54\x54\x53\x57\x51\x5a'\
b'\x4f\x5c\x20\x52\x51\x4a\x52\x4c\x53\x50\x53\x54\x52\x58\x51'\
b'\x5a\x08\x4d\x57\x52\x4a\x52\x50\x20\x52\x4f\x4b\x55\x4f\x20'\
b'\x52\x55\x4b\x4f\x4f\x05\x49\x5b\x52\x4c\x52\x58\x20\x52\x4c'\
b'\x52\x58\x52\x07\x4e\x56\x53\x57\x52\x58\x51\x57\x52\x56\x53'\
b'\x57\x53\x59\x51\x5b\x02\x49\x5b\x4c\x52\x58\x52\x05\x4e\x56'\
b'\x52\x56\x51\x57\x52\x58\x53\x57\x52\x56\x02\x4b\x59\x4b\x5e'\
b'\x59\x46\x1b\x4c\x59\x51\x4b\x4f\x4c\x4e\x4f\x4e\x54\x4f\x57'\
b'\x51\x58\x54\x58\x56\x57\x57\x54\x57\x4f\x56\x4c\x54\x4b\x51'\
b'\x4b\x20\x52\x51\x4b\x50\x4c\x4f\x4f\x4f\x54\x50\x57\x51\x58'\
b'\x20\x52\x54\x58\x55\x57\x56\x54\x56\x4f\x55\x4c\x54\x4b\x09'\
b'\x4c\x59\x50\x4e\x53\x4b\x53\x58\x20\x52\x52\x4c\x52\x58\x20'\
b'\x52\x4f\x58\x56\x58\x22\x4c\x59\x4f\x4d\x4f\x4e\x4e\x4e\x4e'\
b'\x4d\x4f\x4c\x51\x4b\x54\x4b\x56\x4c\x57\x4e\x56\x50\x54\x51'\
b'\x51\x52\x4f\x53\x4e\x55\x4e\x58\x20\x52\x54\x4b\x55\x4c\x56'\
b'\x4e\x55\x50\x54\x51\x20\x52\x4e\x57\x4f\x56\x50\x56\x53\x57'\
b'\x56\x57\x57\x56\x20\x52\x50\x56\x53\x58\x56\x58\x57\x56\x57'\
b'\x55\x26\x4c\x59\x4f\x4d\x4f\x4e\x4e\x4e\x4e\x4d\x4f\x4c\x51'\
b'\x4b\x54\x4b\x56\x4c\x57\x4e\x56\x50\x54\x51\x20\x52\x54\x4b'\
b'\x55\x4c\x56\x4e\x55\x50\x54\x51\x20\x52\x52\x51\x54\x51\x56'\
b'\x52\x57\x54\x57\x55\x56\x57\x54\x58\x51\x58\x4f\x57\x4e\x56'\
b'\x4e\x55\x4f\x55\x4f\x56\x20\x52\x54\x51\x55\x52\x56\x54\x56'\
b'\x55\x55\x57\x54\x58\x0c\x4c\x59\x53\x4d\x53\x58\x20\x52\x54'\
b'\x4b\x54\x58\x20\x52\x54\x4b\x4d\x54\x58\x54\x20\x52\x51\x58'\
b'\x56\x58\x20\x4c\x59\x4f\x4b\x4e\x51\x20\x52\x4f\x4b\x56\x4b'\
b'\x20\x52\x4f\x4c\x53\x4c\x56\x4b\x20\x52\x4e\x51\x4f\x50\x51'\
b'\x4f\x54\x4f\x56\x50\x57\x52\x57\x55\x56\x57\x54\x58\x51\x58'\
b'\x4f\x57\x4e\x56\x4e\x55\x4f\x55\x4f\x56\x20\x52\x54\x4f\x55'\
b'\x50\x56\x52\x56\x55\x55\x57\x54\x58\x23\x4c\x59\x56\x4d\x56'\
b'\x4e\x57\x4e\x57\x4d\x56\x4c\x54\x4b\x52\x4b\x50\x4c\x4f\x4d'\
b'\x4e\x50\x4e\x55\x4f\x57\x51\x58\x54\x58\x56\x57\x57\x55\x57'\
b'\x53\x56\x51\x54\x50\x51\x50\x4e\x52\x20\x52\x52\x4b\x50\x4d'\
b'\x4f\x50\x4f\x55\x50\x57\x51\x58\x20\x52\x54\x58\x55\x57\x56'\
b'\x55\x56\x53\x55\x51\x54\x50\x15\x4c\x59\x4e\x4b\x4e\x4f\x20'\
b'\x52\x56\x4d\x52\x54\x50\x58\x20\x52\x57\x4b\x54\x51\x51\x58'\
b'\x20\x52\x4e\x4d\x50\x4b\x52\x4b\x55\x4d\x20\x52\x4e\x4d\x50'\
b'\x4c\x52\x4c\x55\x4d\x56\x4d\x32\x4c\x59\x51\x4b\x4f\x4c\x4e'\
b'\x4e\x4f\x50\x51\x51\x54\x51\x56\x50\x57\x4e\x56\x4c\x54\x4b'\
b'\x51\x4b\x20\x52\x51\x4b\x50\x4c\x4f\x4e\x50\x50\x51\x51\x20'\
b'\x52\x54\x51\x55\x50\x56\x4e\x55\x4c\x54\x4b\x20\x52\x51\x51'\
b'\x4f\x52\x4e\x54\x4e\x55\x4f\x57\x51\x58\x54\x58\x56\x57\x57'\
b'\x55\x57\x54\x56\x52\x54\x51\x20\x52\x51\x51\x50\x52\x4f\x54'\
b'\x4f\x55\x50\x57\x51\x58\x20\x52\x54\x58\x55\x57\x56\x55\x56'\
b'\x54\x55\x52\x54\x51\x23\x4c\x59\x4f\x56\x4f\x55\x4e\x55\x4e'\
b'\x56\x4f\x57\x51\x58\x53\x58\x55\x57\x56\x56\x57\x53\x57\x4e'\
b'\x56\x4c\x54\x4b\x51\x4b\x4f\x4c\x4e\x4e\x4e\x50\x4f\x52\x51'\
b'\x53\x54\x53\x57\x51\x20\x52\x53\x58\x55\x56\x56\x53\x56\x4e'\
b'\x55\x4c\x54\x4b\x20\x52\x51\x4b\x50\x4c\x4f\x4e\x4f\x50\x50'\
b'\x52\x51\x53\x0b\x4e\x56\x52\x4f\x51\x50\x52\x51\x53\x50\x52'\
b'\x4f\x20\x52\x52\x56\x51\x57\x52\x58\x53\x57\x52\x56\x0d\x4e'\
b'\x56\x52\x4f\x51\x50\x52\x51\x53\x50\x52\x4f\x20\x52\x53\x57'\
b'\x52\x58\x51\x57\x52\x56\x53\x57\x53\x59\x51\x5b\x03\x4a\x5a'\
b'\x57\x4c\x4d\x52\x57\x58\x05\x49\x5b\x4c\x50\x58\x50\x20\x52'\
b'\x4c\x54\x58\x54\x03\x4a\x5a\x4d\x4c\x57\x52\x4d\x58\x1c\x4c'\
b'\x59\x4e\x4e\x4f\x4e\x4f\x4f\x4e\x4f\x4e\x4e\x4f\x4c\x51\x4b'\
b'\x54\x4b\x56\x4c\x57\x4e\x57\x4f\x56\x51\x53\x52\x52\x53\x52'\
b'\x54\x53\x54\x20\x52\x54\x4b\x56\x4d\x56\x50\x55\x51\x53\x52'\
b'\x20\x52\x52\x57\x52\x58\x53\x58\x53\x57\x52\x57\x1c\x4a\x5b'\
b'\x55\x50\x53\x4f\x51\x4f\x50\x51\x50\x52\x51\x54\x53\x54\x55'\
b'\x53\x20\x52\x55\x4f\x55\x53\x56\x54\x58\x54\x59\x52\x59\x51'\
b'\x58\x4e\x56\x4c\x53\x4b\x52\x4b\x4f\x4c\x4d\x4e\x4c\x51\x4c'\
b'\x52\x4d\x55\x4f\x57\x52\x58\x53\x58\x56\x57\x11\x4b\x59\x54'\
b'\x4b\x4b\x58\x20\x52\x53\x4d\x54\x58\x20\x52\x54\x4b\x55\x58'\
b'\x20\x52\x4e\x54\x54\x54\x20\x52\x49\x58\x4e\x58\x20\x52\x52'\
b'\x58\x57\x58\x21\x4a\x59\x50\x4b\x4c\x58\x20\x52\x51\x4b\x4d'\
b'\x58\x20\x52\x4e\x4b\x55\x4b\x57\x4c\x57\x4e\x56\x50\x53\x51'\
b'\x20\x52\x55\x4b\x56\x4c\x56\x4e\x55\x50\x53\x51\x20\x52\x4f'\
b'\x51\x52\x51\x54\x52\x55\x53\x55\x55\x54\x57\x51\x58\x4a\x58'\
b'\x20\x52\x52\x51\x54\x53\x54\x55\x53\x57\x51\x58\x18\x4b\x58'\
b'\x56\x4c\x57\x4c\x58\x4b\x57\x4e\x56\x4c\x54\x4b\x52\x4b\x50'\
b'\x4c\x4f\x4d\x4e\x4f\x4d\x52\x4d\x55\x4e\x57\x50\x58\x52\x58'\
b'\x54\x57\x55\x55\x20\x52\x52\x4b\x50\x4d\x4f\x4f\x4e\x52\x4e'\
b'\x56\x50\x58\x19\x4a\x59\x50\x4b\x4c\x58\x20\x52\x51\x4b\x4d'\
b'\x58\x20\x52\x4e\x4b\x54\x4b\x56\x4c\x57\x4e\x57\x51\x56\x54'\
b'\x55\x56\x54\x57\x51\x58\x4a\x58\x20\x52\x54\x4b\x55\x4c\x56'\
b'\x4e\x56\x51\x55\x54\x54\x56\x53\x57\x51\x58\x15\x4a\x59\x50'\
b'\x4b\x4c\x58\x20\x52\x51\x4b\x4d\x58\x20\x52\x53\x4f\x52\x53'\
b'\x20\x52\x4e\x4b\x58\x4b\x57\x4e\x57\x4b\x20\x52\x4f\x51\x52'\
b'\x51\x20\x52\x4a\x58\x54\x58\x55\x55\x53\x58\x13\x4a\x58\x50'\
b'\x4b\x4c\x58\x20\x52\x51\x4b\x4d\x58\x20\x52\x53\x4f\x52\x53'\
b'\x20\x52\x4e\x4b\x58\x4b\x57\x4e\x57\x4b\x20\x52\x4f\x51\x52'\
b'\x51\x20\x52\x4a\x58\x4f\x58\x20\x4b\x59\x56\x4c\x57\x4c\x58'\
b'\x4b\x57\x4e\x56\x4c\x54\x4b\x52\x4b\x50\x4c\x4f\x4d\x4e\x4f'\
b'\x4d\x52\x4d\x55\x4e\x57\x50\x58\x52\x58\x54\x57\x55\x56\x56'\
b'\x53\x20\x52\x52\x4b\x50\x4d\x4f\x4f\x4e\x52\x4e\x56\x50\x58'\
b'\x20\x52\x52\x58\x54\x56\x55\x53\x20\x52\x53\x53\x58\x53\x1a'\
b'\x4a\x5b\x50\x4b\x4c\x58\x20\x52\x51\x4b\x4d\x58\x20\x52\x58'\
b'\x4b\x54\x58\x20\x52\x59\x4b\x55\x58\x20\x52\x4e\x4b\x53\x4b'\
b'\x20\x52\x56\x4b\x5b\x4b\x20\x52\x4f\x51\x56\x51\x20\x52\x4a'\
b'\x58\x4f\x58\x20\x52\x52\x58\x57\x58\x0b\x4e\x57\x54\x4b\x50'\
b'\x58\x20\x52\x55\x4b\x51\x58\x20\x52\x52\x4b\x57\x4b\x20\x52'\
b'\x4e\x58\x53\x58\x12\x4c\x58\x55\x4b\x52\x55\x51\x57\x50\x58'\
b'\x20\x52\x56\x4b\x53\x55\x52\x57\x50\x58\x4f\x58\x4d\x57\x4c'\
b'\x55\x4d\x54\x4e\x55\x4d\x56\x20\x52\x53\x4b\x58\x4b\x1a\x4a'\
b'\x5a\x50\x4b\x4c\x58\x20\x52\x51\x4b\x4d\x58\x20\x52\x59\x4b'\
b'\x4f\x52\x20\x52\x52\x50\x54\x58\x20\x52\x53\x50\x55\x58\x20'\
b'\x52\x4e\x4b\x53\x4b\x20\x52\x56\x4b\x5b\x4b\x20\x52\x4a\x58'\
b'\x4f\x58\x20\x52\x52\x58\x57\x58\x0d\x4b\x58\x51\x4b\x4d\x58'\
b'\x20\x52\x52\x4b\x4e\x58\x20\x52\x4f\x4b\x54\x4b\x20\x52\x4b'\
b'\x58\x55\x58\x56\x55\x54\x58\x1d\x49\x5c\x4f\x4b\x4b\x58\x20'\
b'\x52\x4f\x4d\x50\x58\x20\x52\x50\x4b\x51\x56\x20\x52\x59\x4b'\
b'\x50\x58\x20\x52\x59\x4b\x55\x58\x20\x52\x5a\x4b\x56\x58\x20'\
b'\x52\x4d\x4b\x50\x4b\x20\x52\x59\x4b\x5c\x4b\x20\x52\x49\x58'\
b'\x4d\x58\x20\x52\x53\x58\x58\x58\x14\x4a\x5a\x50\x4b\x4c\x58'\
b'\x20\x52\x50\x4b\x54\x58\x20\x52\x51\x4b\x54\x55\x20\x52\x58'\
b'\x4b\x54\x58\x20\x52\x4e\x4b\x51\x4b\x20\x52\x56\x4b\x5a\x4b'\
b'\x20\x52\x4a\x58\x4e\x58\x1f\x4b\x59\x52\x4b\x50\x4c\x4f\x4d'\
b'\x4e\x4f\x4d\x52\x4d\x55\x4e\x57\x50\x58\x52\x58\x54\x57\x55'\
b'\x56\x56\x54\x57\x51\x57\x4e\x56\x4c\x54\x4b\x52\x4b\x20\x52'\
b'\x52\x4b\x50\x4d\x4f\x4f\x4e\x52\x4e\x56\x50\x58\x20\x52\x52'\
b'\x58\x54\x56\x55\x54\x56\x51\x56\x4d\x54\x4b\x17\x4a\x59\x50'\
b'\x4b\x4c\x58\x20\x52\x51\x4b\x4d\x58\x20\x52\x4e\x4b\x55\x4b'\
b'\x57\x4c\x58\x4d\x58\x4f\x57\x51\x54\x52\x4f\x52\x20\x52\x55'\
b'\x4b\x57\x4d\x57\x4f\x56\x51\x54\x52\x20\x52\x4a\x58\x4f\x58'\
b'\x2d\x4b\x59\x52\x4b\x50\x4c\x4f\x4d\x4e\x4f\x4d\x52\x4d\x55'\
b'\x4e\x57\x50\x58\x52\x58\x54\x57\x55\x56\x56\x54\x57\x51\x57'\
b'\x4e\x56\x4c\x54\x4b\x52\x4b\x20\x52\x52\x4b\x50\x4d\x4f\x4f'\
b'\x4e\x52\x4e\x56\x50\x58\x20\x52\x52\x58\x54\x56\x55\x54\x56'\
b'\x51\x56\x4d\x54\x4b\x20\x52\x4f\x57\x4f\x56\x50\x55\x51\x55'\
b'\x52\x56\x52\x5a\x53\x5b\x54\x5b\x55\x5a\x20\x52\x52\x56\x53'\
b'\x5a\x54\x5b\x22\x4a\x5a\x50\x4b\x4c\x58\x20\x52\x51\x4b\x4d'\
b'\x58\x20\x52\x4e\x4b\x55\x4b\x57\x4c\x58\x4d\x58\x4f\x57\x51'\
b'\x54\x52\x4f\x52\x20\x52\x55\x4b\x57\x4d\x57\x4f\x56\x51\x54'\
b'\x52\x20\x52\x53\x52\x54\x57\x55\x58\x56\x58\x57\x57\x20\x52'\
b'\x53\x52\x54\x53\x55\x57\x56\x58\x20\x52\x4a\x58\x4f\x58\x1b'\
b'\x4b\x5a\x57\x4c\x58\x4c\x59\x4b\x58\x4e\x57\x4c\x55\x4b\x52'\
b'\x4b\x50\x4c\x4f\x4d\x4f\x4f\x50\x50\x55\x53\x56\x54\x20\x52'\
b'\x4f\x4e\x50\x4f\x55\x52\x56\x53\x56\x56\x55\x57\x53\x58\x50'\
b'\x58\x4e\x57\x4d\x55\x4c\x58\x4d\x57\x4e\x57\x0f\x4b\x5a\x54'\
b'\x4b\x50\x58\x20\x52\x55\x4b\x51\x58\x20\x52\x50\x4b\x4e\x4e'\
b'\x4f\x4b\x5a\x4b\x59\x4e\x59\x4b\x20\x52\x4e\x58\x53\x58\x13'\
b'\x4a\x5b\x50\x4b\x4d\x55\x4d\x57\x4f\x58\x53\x58\x55\x57\x56'\
b'\x55\x59\x4b\x20\x52\x51\x4b\x4e\x55\x4e\x57\x4f\x58\x20\x52'\
b'\x4e\x4b\x53\x4b\x20\x52\x57\x4b\x5b\x4b\x0e\x4b\x59\x4f\x4b'\
b'\x50\x58\x20\x52\x50\x4b\x51\x56\x20\x52\x59\x4b\x50\x58\x20'\
b'\x52\x4d\x4b\x52\x4b\x20\x52\x56\x4b\x5b\x4b\x17\x49\x5b\x4e'\
b'\x4b\x4d\x58\x20\x52\x4f\x4b\x4e\x56\x20\x52\x54\x4b\x4d\x58'\
b'\x20\x52\x54\x4b\x53\x58\x20\x52\x55\x4b\x54\x56\x20\x52\x5a'\
b'\x4b\x53\x58\x20\x52\x4c\x4b\x51\x4b\x20\x52\x58\x4b\x5c\x4b'\
b'\x14\x4b\x5a\x50\x4b\x54\x58\x20\x52\x51\x4b\x55\x58\x20\x52'\
b'\x59\x4b\x4c\x58\x20\x52\x4e\x4b\x53\x4b\x20\x52\x56\x4b\x5b'\
b'\x4b\x20\x52\x4a\x58\x4f\x58\x20\x52\x52\x58\x57\x58\x13\x4c'\
b'\x59\x50\x4b\x52\x51\x50\x58\x20\x52\x51\x4b\x53\x51\x20\x52'\
b'\x59\x4b\x53\x51\x51\x58\x20\x52\x4e\x4b\x53\x4b\x20\x52\x56'\
b'\x4b\x5b\x4b\x20\x52\x4e\x58\x53\x58\x0f\x4c\x59\x58\x4b\x4c'\
b'\x58\x20\x52\x59\x4b\x4d\x58\x20\x52\x51\x4b\x4f\x4e\x50\x4b'\
b'\x59\x4b\x20\x52\x4c\x58\x55\x58\x56\x55\x54\x58\x0b\x4d\x57'\
b'\x50\x48\x50\x5c\x20\x52\x51\x48\x51\x5c\x20\x52\x50\x48\x55'\
b'\x48\x20\x52\x50\x5c\x55\x5c\x02\x4b\x59\x4b\x46\x59\x5e\x0b'\
b'\x4d\x57\x53\x48\x53\x5c\x20\x52\x54\x48\x54\x5c\x20\x52\x4f'\
b'\x48\x54\x48\x20\x52\x4f\x5c\x54\x5c\x0c\x4d\x57\x52\x4d\x52'\
b'\x58\x20\x52\x4f\x50\x50\x4f\x52\x4c\x54\x4f\x55\x50\x20\x52'\
b'\x50\x4f\x52\x4d\x54\x4f\x02\x4a\x5a\x4a\x5a\x5a\x5a\x07\x4e'\
b'\x56\x53\x4b\x51\x4d\x51\x4f\x52\x50\x53\x4f\x52\x4e\x51\x4f'\
b'\x1f\x4b\x5a\x56\x4f\x54\x56\x54\x57\x55\x58\x57\x58\x58\x57'\
b'\x59\x55\x20\x52\x57\x4f\x55\x56\x55\x57\x56\x58\x20\x52\x55'\
b'\x53\x55\x51\x53\x4f\x51\x4f\x4f\x50\x4e\x51\x4d\x53\x4d\x55'\
b'\x4e\x57\x50\x58\x52\x58\x54\x56\x20\x52\x51\x4f\x4f\x51\x4e'\
b'\x53\x4e\x56\x50\x58\x1f\x4a\x58\x4f\x4b\x4d\x52\x20\x52\x50'\
b'\x4b\x4e\x52\x4e\x56\x50\x58\x20\x52\x4e\x52\x4f\x50\x51\x4f'\
b'\x53\x4f\x55\x50\x56\x52\x56\x54\x55\x56\x54\x57\x52\x58\x50'\
b'\x58\x4e\x57\x4d\x55\x4d\x52\x20\x52\x53\x4f\x55\x51\x55\x54'\
b'\x54\x56\x52\x58\x20\x52\x4d\x4b\x50\x4b\x15\x4b\x58\x55\x50'\
b'\x55\x51\x56\x51\x55\x50\x53\x4f\x51\x4f\x4f\x50\x4e\x51\x4d'\
b'\x53\x4d\x55\x4e\x57\x50\x58\x52\x58\x54\x57\x55\x56\x20\x52'\
b'\x51\x4f\x4f\x51\x4e\x53\x4e\x56\x50\x58\x22\x4b\x5a\x57\x4b'\
b'\x54\x56\x54\x57\x55\x58\x57\x58\x58\x57\x59\x55\x20\x52\x58'\
b'\x4b\x55\x56\x55\x57\x56\x58\x20\x52\x55\x53\x55\x51\x53\x4f'\
b'\x51\x4f\x4f\x50\x4e\x51\x4d\x53\x4d\x55\x4e\x57\x50\x58\x52'\
b'\x58\x54\x56\x20\x52\x51\x4f\x4f\x51\x4e\x53\x4e\x56\x50\x58'\
b'\x20\x52\x55\x4b\x58\x4b\x16\x4b\x57\x4e\x55\x52\x54\x54\x53'\
b'\x55\x52\x55\x50\x53\x4f\x51\x4f\x4f\x50\x4e\x51\x4d\x53\x4d'\
b'\x55\x4e\x57\x50\x58\x52\x58\x54\x57\x55\x56\x20\x52\x51\x4f'\
b'\x4f\x51\x4e\x53\x4e\x56\x50\x58\x16\x4d\x58\x57\x4b\x58\x4c'\
b'\x58\x4b\x56\x4b\x54\x4c\x53\x4e\x50\x59\x4f\x5b\x4e\x5c\x20'\
b'\x52\x56\x4b\x55\x4c\x54\x4e\x51\x59\x50\x5b\x4e\x5c\x4c\x5c'\
b'\x4c\x5b\x4d\x5c\x20\x52\x50\x4f\x56\x4f\x21\x4b\x59\x56\x4f'\
b'\x54\x56\x53\x59\x52\x5b\x20\x52\x57\x4f\x55\x56\x54\x59\x52'\
b'\x5b\x50\x5c\x4d\x5c\x4c\x5b\x4d\x5b\x4e\x5c\x20\x52\x55\x53'\
b'\x55\x51\x53\x4f\x51\x4f\x4f\x50\x4e\x51\x4d\x53\x4d\x55\x4e'\
b'\x57\x50\x58\x52\x58\x54\x56\x20\x52\x51\x4f\x4f\x51\x4e\x53'\
b'\x4e\x56\x50\x58\x1c\x4b\x5a\x50\x4b\x4c\x58\x20\x52\x51\x4b'\
b'\x4d\x58\x20\x52\x4f\x51\x50\x50\x52\x4f\x54\x4f\x56\x50\x56'\
b'\x52\x55\x55\x55\x57\x56\x58\x20\x52\x54\x4f\x55\x50\x55\x52'\
b'\x54\x55\x54\x57\x55\x58\x57\x58\x58\x57\x59\x55\x20\x52\x4e'\
b'\x4b\x51\x4b\x19\x4d\x57\x53\x4b\x53\x4c\x54\x4c\x54\x4b\x53'\
b'\x4b\x20\x52\x4e\x52\x4f\x50\x50\x4f\x52\x4f\x53\x50\x53\x52'\
b'\x52\x55\x52\x57\x53\x58\x20\x52\x51\x4f\x52\x50\x52\x52\x51'\
b'\x55\x51\x57\x52\x58\x54\x58\x55\x57\x56\x55\x19\x4d\x57\x54'\
b'\x4b\x54\x4c\x55\x4c\x55\x4b\x54\x4b\x20\x52\x4f\x52\x50\x50'\
b'\x51\x4f\x53\x4f\x54\x50\x54\x52\x52\x59\x51\x5b\x4f\x5c\x4d'\
b'\x5c\x4d\x5b\x4e\x5c\x20\x52\x52\x4f\x53\x50\x53\x52\x51\x59'\
b'\x50\x5b\x4f\x5c\x1f\x4b\x58\x50\x4b\x4c\x58\x20\x52\x51\x4b'\
b'\x4d\x58\x20\x52\x56\x50\x55\x51\x56\x51\x56\x50\x55\x4f\x54'\
b'\x4f\x52\x51\x50\x52\x4f\x52\x20\x52\x4f\x52\x50\x53\x51\x57'\
b'\x52\x58\x54\x58\x55\x57\x56\x55\x20\x52\x4f\x52\x51\x53\x52'\
b'\x57\x53\x58\x20\x52\x4e\x4b\x51\x4b\x0f\x4e\x56\x53\x4b\x50'\
b'\x56\x50\x57\x51\x58\x53\x58\x54\x57\x55\x55\x20\x52\x54\x4b'\
b'\x51\x56\x51\x57\x52\x58\x20\x52\x51\x4b\x54\x4b\x2d\x46\x5e'\
b'\x47\x52\x48\x50\x49\x4f\x4b\x4f\x4c\x50\x4c\x51\x4a\x58\x20'\
b'\x52\x4a\x4f\x4b\x50\x4b\x51\x49\x58\x20\x52\x4c\x51\x4d\x50'\
b'\x4f\x4f\x51\x4f\x53\x50\x53\x51\x51\x58\x20\x52\x51\x4f\x52'\
b'\x50\x52\x51\x50\x58\x20\x52\x53\x51\x54\x50\x56\x4f\x58\x4f'\
b'\x5a\x50\x5a\x52\x59\x55\x59\x57\x5a\x58\x20\x52\x58\x4f\x59'\
b'\x50\x59\x52\x58\x55\x58\x57\x59\x58\x5b\x58\x5c\x57\x5d\x55'\
b'\x20\x4a\x5b\x4b\x52\x4c\x50\x4d\x4f\x4f\x4f\x50\x50\x50\x51'\
b'\x4e\x58\x20\x52\x4e\x4f\x4f\x50\x4f\x51\x4d\x58\x20\x52\x50'\
b'\x51\x51\x50\x53\x4f\x55\x4f\x57\x50\x57\x52\x56\x55\x56\x57'\
b'\x57\x58\x20\x52\x55\x4f\x56\x50\x56\x52\x55\x55\x55\x57\x56'\
b'\x58\x58\x58\x59\x57\x5a\x55\x1b\x4b\x58\x51\x4f\x4f\x50\x4e'\
b'\x51\x4d\x53\x4d\x55\x4e\x57\x50\x58\x52\x58\x54\x57\x55\x56'\
b'\x56\x54\x56\x52\x55\x50\x53\x4f\x51\x4f\x20\x52\x51\x4f\x4f'\
b'\x51\x4e\x53\x4e\x56\x50\x58\x20\x52\x52\x58\x54\x56\x55\x54'\
b'\x55\x51\x53\x4f\x22\x4a\x59\x4b\x52\x4c\x50\x4d\x4f\x4f\x4f'\
b'\x50\x50\x50\x51\x4d\x5c\x20\x52\x4e\x4f\x4f\x50\x4f\x51\x4c'\
b'\x5c\x20\x52\x50\x51\x52\x4f\x54\x4f\x56\x50\x57\x52\x57\x54'\
b'\x56\x56\x55\x57\x53\x58\x51\x58\x4f\x56\x4f\x54\x20\x52\x54'\
b'\x4f\x56\x51\x56\x54\x55\x56\x53\x58\x20\x52\x4a\x5c\x4f\x5c'\
b'\x1b\x4b\x59\x56\x4f\x52\x5c\x20\x52\x57\x4f\x53\x5c\x20\x52'\
b'\x55\x53\x55\x51\x53\x4f\x51\x4f\x4f\x50\x4e\x51\x4d\x53\x4d'\
b'\x55\x4e\x57\x50\x58\x52\x58\x54\x56\x20\x52\x51\x4f\x4f\x51'\
b'\x4e\x53\x4e\x56\x50\x58\x20\x52\x50\x5c\x55\x5c\x15\x4c\x58'\
b'\x4d\x52\x4e\x50\x4f\x4f\x51\x4f\x52\x50\x52\x51\x50\x58\x20'\
b'\x52\x50\x4f\x51\x50\x51\x51\x4f\x58\x20\x52\x52\x51\x53\x50'\
b'\x55\x4f\x56\x4f\x57\x50\x57\x51\x56\x51\x57\x50\x17\x4c\x59'\
b'\x56\x50\x56\x51\x57\x51\x56\x50\x54\x4f\x51\x4f\x4f\x50\x4f'\
b'\x52\x51\x53\x54\x54\x56\x55\x20\x52\x4f\x51\x51\x52\x54\x53'\
b'\x56\x54\x56\x57\x54\x58\x51\x58\x4f\x57\x4e\x56\x4f\x56\x4f'\
b'\x57\x0f\x4e\x57\x53\x4b\x50\x56\x50\x57\x51\x58\x53\x58\x54'\
b'\x57\x55\x55\x20\x52\x54\x4b\x51\x56\x51\x57\x52\x58\x20\x52'\
b'\x50\x4f\x55\x4f\x20\x49\x5a\x4a\x52\x4b\x50\x4c\x4f\x4e\x4f'\
b'\x4f\x50\x4f\x52\x4e\x55\x4e\x57\x4f\x58\x20\x52\x4d\x4f\x4e'\
b'\x50\x4e\x52\x4d\x55\x4d\x57\x4f\x58\x51\x58\x53\x57\x54\x56'\
b'\x20\x52\x56\x4f\x54\x56\x54\x57\x55\x58\x57\x58\x58\x57\x59'\
b'\x55\x20\x52\x57\x4f\x55\x56\x55\x57\x56\x58\x17\x4a\x58\x4b'\
b'\x52\x4c\x50\x4d\x4f\x4f\x4f\x50\x50\x50\x52\x4f\x55\x4f\x57'\
b'\x50\x58\x20\x52\x4e\x4f\x4f\x50\x4f\x52\x4e\x55\x4e\x57\x50'\
b'\x58\x51\x58\x53\x57\x55\x55\x56\x52\x56\x4f\x55\x4f\x56\x50'\
b'\x24\x48\x5c\x49\x52\x4a\x50\x4b\x4f\x4d\x4f\x4e\x50\x4e\x52'\
b'\x4d\x55\x4d\x57\x4e\x58\x20\x52\x4c\x4f\x4d\x50\x4d\x52\x4c'\
b'\x55\x4c\x57\x4e\x58\x4f\x58\x51\x57\x52\x56\x20\x52\x54\x4f'\
b'\x52\x56\x52\x57\x54\x58\x20\x52\x55\x4f\x53\x56\x53\x57\x54'\
b'\x58\x55\x58\x57\x57\x59\x55\x5a\x52\x5a\x4f\x59\x4f\x5a\x50'\
b'\x25\x4a\x5a\x4d\x52\x4e\x50\x50\x4f\x52\x4f\x53\x50\x53\x52'\
b'\x20\x52\x51\x4f\x52\x50\x52\x52\x51\x55\x50\x57\x4e\x58\x4d'\
b'\x58\x4c\x57\x4c\x56\x4d\x56\x4c\x57\x20\x52\x58\x50\x57\x51'\
b'\x58\x51\x58\x50\x57\x4f\x56\x4f\x54\x50\x53\x52\x52\x55\x52'\
b'\x57\x53\x58\x20\x52\x51\x55\x51\x57\x52\x58\x54\x58\x56\x57'\
b'\x57\x55\x22\x49\x59\x4a\x52\x4b\x50\x4c\x4f\x4e\x4f\x4f\x50'\
b'\x4f\x52\x4e\x55\x4e\x57\x4f\x58\x20\x52\x4d\x4f\x4e\x50\x4e'\
b'\x52\x4d\x55\x4d\x57\x4f\x58\x51\x58\x53\x57\x54\x56\x20\x52'\
b'\x56\x4f\x54\x56\x53\x59\x52\x5b\x20\x52\x57\x4f\x55\x56\x54'\
b'\x59\x52\x5b\x50\x5c\x4d\x5c\x4c\x5b\x4d\x5b\x4e\x5c\x1a\x4b'\
b'\x59\x57\x4f\x57\x50\x56\x51\x4e\x56\x4d\x57\x4d\x58\x20\x52'\
b'\x4e\x51\x4f\x4f\x52\x4f\x55\x51\x20\x52\x4f\x50\x52\x50\x55'\
b'\x51\x56\x51\x20\x52\x4e\x56\x4f\x56\x52\x57\x55\x57\x20\x52'\
b'\x4f\x56\x52\x58\x55\x58\x56\x56\x25\x4c\x57\x53\x48\x51\x49'\
b'\x50\x4a\x50\x4c\x52\x4e\x53\x50\x20\x52\x51\x49\x50\x4c\x20'\
b'\x52\x53\x4e\x52\x51\x20\x52\x50\x4a\x51\x4c\x53\x4e\x53\x50'\
b'\x52\x51\x50\x52\x52\x53\x53\x54\x53\x56\x51\x58\x50\x5a\x20'\
b'\x52\x52\x53\x53\x56\x20\x52\x50\x58\x51\x5b\x20\x52\x53\x54'\
b'\x52\x56\x50\x58\x50\x5a\x51\x5b\x53\x5c\x02\x4f\x55\x52\x48'\
b'\x52\x5c\x25\x4d\x58\x51\x48\x53\x49\x54\x4a\x54\x4c\x52\x4e'\
b'\x51\x50\x20\x52\x53\x49\x54\x4c\x20\x52\x51\x4e\x52\x51\x20'\
b'\x52\x54\x4a\x53\x4c\x51\x4e\x51\x50\x52\x51\x54\x52\x52\x53'\
b'\x51\x54\x51\x56\x53\x58\x54\x5a\x20\x52\x52\x53\x51\x56\x20'\
b'\x52\x54\x58\x53\x5b\x20\x52\x51\x54\x52\x56\x54\x58\x54\x5a'\
b'\x53\x5b\x51\x5c\x0f\x4a\x5a\x4c\x54\x4c\x52\x4d\x50\x4f\x50'\
b'\x55\x53\x57\x53\x58\x52\x20\x52\x4c\x52\x4d\x51\x4f\x51\x55'\
b'\x54\x57\x54\x58\x52\x58\x50\x09\x4d\x57\x51\x4b\x50\x4c\x50'\
b'\x4e\x51\x4f\x53\x4f\x54\x4e\x54\x4c\x53\x4b\x51\x4b'

_index =\
b'\x00\x00\x03\x00\x22\x00\x3f\x00\x58\x00\x9d\x00\xd2\x00\x25'\
b'\x01\x36\x01\x57\x01\x78\x01\x8b\x01\x98\x01\xa9\x01\xb0\x01'\
b'\xbd\x01\xc4\x01\xfd\x01\x12\x02\x59\x02\xa8\x02\xc3\x02\x06'\
b'\x03\x4f\x03\x7c\x03\xe3\x03\x2c\x04\x45\x04\x62\x04\x6b\x04'\
b'\x78\x04\x81\x04\xbc\x04\xf7\x04\x1c\x05\x61\x05\x94\x05\xc9'\
b'\x05\xf6\x05\x1f\x06\x62\x06\x99\x06\xb2\x06\xd9\x06\x10\x07'\
b'\x2d\x07\x6a\x07\x95\x07\xd6\x07\x07\x08\x64\x08\xab\x08\xe4'\
b'\x08\x05\x09\x2e\x09\x4d\x09\x7e\x09\xa9\x09\xd2\x09\xf3\x09'\
b'\x0c\x0a\x13\x0a\x2c\x0a\x47\x0a\x4e\x0a\x5f\x0a\xa0\x0a\xe1'\
b'\x0a\x0e\x0b\x55\x0b\x84\x0b\xb3\x0b\xf8\x0b\x33\x0c\x68\x0c'\
b'\x9d\x0c\xde\x0c\xff\x0c\x5c\x0d\x9f\x0d\xd8\x0d\x1f\x0e\x58'\
b'\x0e\x85\x0e\xb6\x0e\xd7\x0e\x1a\x0f\x4b\x0f\x96\x0f\xe3\x0f'\
b'\x2a\x10\x61\x10\xae\x10\xb5\x10\x02\x11\x23\x11'

INDEX = memoryview(_index)
FONT = memoryview(_font)
