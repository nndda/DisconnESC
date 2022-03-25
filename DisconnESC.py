import wmi
import keyboard

wql = "SELECT * FROM __InstanceDeletionEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_Keyboard\'"

dw = wmi.WMI().watch_for(raw_wql=wql)
n = 0

while 1:
    try:
        ds = dw(timeout_ms=0)
    except wmi.x_wmi_timed_out:
        pass
    else:
        if ds:
            n = n + 1

    if n == 1:
        print("-")
        keyboard.press_and_release('esc')
    if n >= 4:
        n = 0
